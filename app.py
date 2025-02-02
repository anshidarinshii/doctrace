from website import create_app

if __name__ == "__main__":
    app = create_app()
    # whenever there will be a change in python it will auto rerun flask server
    app.run(debug=True)