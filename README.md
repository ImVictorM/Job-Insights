# Job Insights 📈

## Project Context 💡
That was my first project using the language Python. In this project, I made some analysis based on a set of jobs data `(data/jobs.csv)` implementing functions and incorporating them into a web app using Flask. To ensure the correctness of some functionalities, I also made some tests to functionalities using the pytest lib.

### Acquired Knowledge 📖
In this project, I was able to:
- Use conditional and loop structures.
- Use Python's built-in functions.
- handle exceptions.
- Manipulate files.
- Write functions.
- Testing with Pytest.
- Write modules and import them into another code.

## Main Technologies 🧰
<table>
    <thead>
        <tr>
            <th>Python</th>
            <th>Pytest</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">
               <a href="https://www.python.org" target="_blank" rel="noreferrer"> 
                   <img 
                       src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" 
                       alt="python" 
                       width="40" 
                       height="40"
                    /> 
                </a>
            </td>
            <td align="center">
                <a href="https://docs.pytest.org/en/7.3.x/" target="_blank" rel="noreferrer"> 
                   <img 
                       src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pytest_logo.svg/200px-Pytest_logo.svg.png" 
                       alt="pytest" 
                       width="40" 
                       height="40"
                    /> 
                </a>
            </td>
        </tr>
    </tbody>
</table>

## Running the application ⚙️

1. Clone the repository and enter it
```
git clone git@github.com:ImVictorM/Job-Insights.git && cd Job-Insights
```
 
2. Create the virtual environment
```
python3 -m venv .venv && source .venv/bin/activate
```
3. Install the dependencies
```
python3 -m pip install -r dev-requirements.txt
```
4. Run the application
```
flask run
```
Follow the link to see the app running:
http://localhost:5000

## Testing 🛠️
To run all tests:
```
python3 -m pytest
```
Running only one test file:
```
python3 -m pytest {test_file_path}.py
```
