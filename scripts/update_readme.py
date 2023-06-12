import calendar
import os
import re
from datetime import datetime, timedelta

import requests
from tabulate import tabulate


class UpdateReadme:
    BASE_URL = "https://leetcode.com/graphql/"

    stat_info = {
        "language": {
            "payload": {
                "query": "\n    query languageStats($username: String!) {\n  matchedUser(username: $username) {\n    languageProblemCount {\n      languageName\n      problemsSolved\n    }\n  }\n}\n    ",
                "variables": {"username": "CaedenPH"},
                "operationName": "languageStats",
            },
            "response": ["languageProblemCount"],
        },
        "difficulty": {
            "payload": {
                "query": "\n    query userProblemsSolved($username: String!) {\n  allQuestionsCount {\n    difficulty\n    count\n  }\n  matchedUser(username: $username) {\n    problemsSolvedBeatsStats {\n      difficulty\n      percentage\n    }\n    submitStatsGlobal {\n      acSubmissionNum {\n        difficulty\n        count\n      }\n    }\n  }\n}\n    ",
                "variables": {"username": "CaedenPH"},
                "operationName": "userProblemsSolved",
            },
            "response": ["submitStatsGlobal", "acSubmissionNum"],
        },
        "topic": {
            "payload": {
                "query": "\n    query skillStats($username: String!) {\n  matchedUser(username: $username) {\n    tagProblemCounts {\n      advanced {\n        tagName\n        tagSlug\n        problemsSolved\n      }\n      intermediate {\n        tagName\n        tagSlug\n        problemsSolved\n      }\n      fundamental {\n        tagName\n        tagSlug\n        problemsSolved\n      }\n    }\n  }\n}\n    ",
                "variables": {"username": "CaedenPH"},
                "operationName": "skillStats",
            },
            "response": ["tagProblemCounts"],
        },
    }

    def get_graphql_data(self, stat: str) -> dict:
        """
        Gets the data from the GraphQL API for the given stat.

        :param stat: The stat to get the data for
        :return: The data in the format [{**y, problemsSolved: 1}]
        """
        payload, response = self.stat_info[stat].values()
        request = requests.get(self.BASE_URL, json=payload)
        request.raise_for_status()

        data = request.json()["data"]["matchedUser"]
        for key in response:  # Dynamically key into response
            data: list[dict] | dict[str, list[dict]] = data[key]

        if stat == "difficulty":
            # The response for difficulties uses count instead of problemsSolved
            [d.__setitem__("problemsSolved", d.pop("count")) for d in data]
        elif stat == "topic":
            # For topics, data = {'easy': [{x: y, problemsSolved: 1}]}
            # so we need to take out the level and place it into the list
            # such that data = {[x: y, problemsSolved: 1, level: 'easy']}
            temp_data = []
            for level, topics in data.items():
                for topic in topics:
                    del topic["tagSlug"]
                    temp_data.append({**topic, "level": level})
            data = temp_data

        # Flatten data[i] dict into a list
        for i in range(len(data)):
            data[i] = list(data[i].values())
        return data

    def get_daily_challenges(self, month: str) -> int:
        """
        Gets the number of daily challenges in the month from the local directory
        of daily challenge solutions.

        :param month: The month to get the number of daily challenges from
        :return: The number of daily challenges in the month
        """
        try:
            files = os.listdir(f"./Daily Challenges/2023/{month.capitalize()}")
            return len(list(filter(lambda f: re.match(r"day_\d{1,2}.py", f), files)))
        except FileNotFoundError:
            return 0

    def table(self, name: str, data: list[str | int], headers: list[str]) -> str:
        """
        Generates a table in Markdown format.

        :param name: The name of the table
        :param data: The data to be displayed in the table
        :param headers: The headers of the table
        :return: The table in Markdown format
        """
        return f"#### {name}\n" + tabulate(data, headers, tablefmt="github", showindex=False)

    def generate_statistics(self) -> str:
        """
        Generates the statistics for the README.

        :return: The statistics in Markdown format
        """
        tables, data = [], []
        # Daily challenges
        for i in range(3):
            month = calendar.month_name[(datetime.now() - timedelta(days=31 * i)).month]
            data.append([month, str(self.get_daily_challenges(month))])
        tables.append(self.table("Daily challenges by month", data, ["Month", "Daily Challenges"]))

        # GraphQL statistics
        for query_topic in self.stat_info:
            headers = [query_topic.capitalize(), "Number of Problems"]
            if query_topic == "topic":
                headers.append("Level")

            data = self.get_graphql_data(query_topic)
            tables.append(self.table(f"Total problems by {query_topic}", data, headers))
        return "\n\n".join(tables)

    def print_readme(self) -> None:
        """
        Prints the README with the updated statistics.
        Used with the linux tee command to update the README content.
        """
        with open("README.md", "r", encoding="utf-8") as readme:
            content = readme.read()

        before_statistics = content.split("### Statistics")[0]
        with open("README.md", "w", encoding="utf-8") as readme:
            readme.write(before_statistics + "\n### Statistics\n" + self.generate_statistics())


if __name__ == "__main__":
    UpdateReadme().print_readme()
