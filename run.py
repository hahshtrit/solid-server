from __init__ import app

if __name__ == "__main__":
    # enabling threading fixes 403 error on chrome, i think
    # nvm, it doesn't work, idk
    app.run(host="0.0.0.0", port=80, debug=True, threaded=True)

import routes

# to run with docker, ensure that the url in browser is 127.0.0.1:8080
# at least that worked for abi