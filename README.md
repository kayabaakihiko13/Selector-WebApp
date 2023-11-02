# Selector-WebApp

Welcome to the **Selector-WebApp** project! This project is an extension of my previous work, aptly named `selector`. It builds upon the foundations laid in the original project and takes it a step further, transitioning from a simple waifu classification program to a fully functional web application.

## Project Overview

The primary objective of this project is to demonstrate the evolution of a concept from a standalone program to a user-friendly web application. It showcases the journey of transforming a command-line tool into an interactive and accessible web experience.

### Key Features

- **Waifu Classification**: The core functionality of the application revolves around classifying waifus. Users can upload images, and the application uses machine learning models to categorize the waifus.

- **User-Friendly Interface**: We have incorporated a sleek and intuitive web interface using FastAPI and Jinja2 templates, making it easy for users to interact with the application.

- **Image Upload**: Users can easily upload images of waifus, which are then processed and classified.

- **Randomized Image Names**: For enhanced security and organization, we've implemented a feature to generate random file names for uploaded images.

- **Static File Serving**: Static files like CSS, JavaScript, and uploaded images are served efficiently to enhance the user experience.

- **Scalability**: The project demonstrates the use of FastAPI for building a robust and scalable web application, capable of handling various functionalities and serving multiple users.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine.

2. Install the project's dependencies using `pip`:

   ```bash
   pip install -r requirements.txt```


3. Run the FastAPI application using Uvicorn, as demonstrated in the project's `main.py`.
   ```bash
   python3 app/main.py
   ```

4. Access the web application via your web browser at `http://127.0.0.1:8000` by default.

## Contributing

Contributions to this project are welcome. If you have any ideas, feature requests, or bug reports, please feel free to open an issue or submit a pull request. We appreciate your input and collaboration in making this project better!

## License

This project is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of the license.

## Acknowledgments

We would like to extend our appreciation to the FastAPI, Jinja2, and Uvicorn communities for their excellent tools and documentation. Without them, this project wouldn't have been possible.

Happy waifu classification and web app development!

---

For more details about the `selector` project, check out the original [repository](https://github.com/your-username/selector).
