# To visually edit your `profile` file you can run
# > notepad $PROFILE 

$func = 'function cs($file) {
    if (!(Test-Path dist)) {
        mkdir dist
    }
    csc /out:dist/program.exe $file
    cls
    ./dist/program.exe
}'
Add-Content $PROFILE $func

