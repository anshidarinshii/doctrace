from website import create_app

if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
    # whenever there will be a change in python it will auto rerun flask server
    app.run(debug=True)