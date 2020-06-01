from reqecho import echo

echo.run(
    host = '0.0.0.0',
    threaded = True,
    debug = True,
    port = 8080
)
