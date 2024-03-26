# Database-Chat-Bot

## Project Description

The "Database-Chat-Bot" project is an application that allows users to query SQL in natural language and display the results in a user-friendly manner. It leverages Anthropics' AI technology _(`Claude`)_ to translate natural language into SQL queries. The application is written in Python and uses Flask for the web framework and `pymssql` for the database connection.

> _Note:_ This is currently only working with **MS SQL Server**. You can easily change the database connection in the `app.py` file and using another module than `pymssql`.

> _Keep in mind:_ This was implemented with Claude, but could be easily replaced with **OpenAI GPT-3**.

## Example

<video src="video/demo-video.mp4" controls></video>

## Using the Project via Docker-Compose

To use the project with Docker-Compose, follow these steps:

1. Ensure that Docker and Docker-Compose are installed on your system.
2. Clone the repository and navigate to the project directory.
3. Run the command `docker-compose up`. This will start the application and all related services.
4. The application is now accessible at `http://localhost:5070`.

## Using the Project without Docker-Compose only with Python

To use the project without Docker-Compose but only with Python, follow these steps:

1. Ensure that Python 3.10 is installed on your system.
2. Clone the repository and navigate to the project directory.
3. Install the required Python packages with the command `pip install -r requirements.txt`.
4. Start the application with the command `python app.py`.
5. The application is now accessible at `http://localhost:5000`.

## License

This project is licensed under the MIT License. For more information, refer to the [License file](https://opensource.org/licenses/MIT).

## Author

This project was created by Michael Muyakwa.

## Notes for Project Development

This project was created to explore the capabilities of Anthropics' AI technology. In the future, a version with OpenAI GPT-3 could be implemented. Contributions are welcome if you are interested in further developing this project.

> _See also:_ [Docker-Compose](https://www.google.com/search?q=docker-compose), [Python](https://www.google.com/search?q=python), [Flask](https://www.google.com/search?q=flask), [pymssql](https://www.google.com/search?q=pymssql), [Anthropics](https://www.google.com/search?q=anthropics)
> _You may also enjoy:_ [SQL](https://www.google.com/search?q=sql), [AI Technology](https://www.google.com/search?q=ai-technology), [OpenAI GPT-3](https://www.google.com/search?q=openai+gpt-3)
