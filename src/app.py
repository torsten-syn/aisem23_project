from project_web.index import app

server = app.server

if __name__ == "__main__":
    print("="*60)
    print("To see the results go to your browser, type localhost:8053 in the address line and run a search for SMILES.")
    print("If everything runs correct, you will see the histogram appearing in the results after pressing a SEARCH button.")
    print("="*60)
    app.run_server(debug=True, host="127.0.0.1", port=8053, use_reloader=True)