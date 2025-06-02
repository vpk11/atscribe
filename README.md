# ATScribe - AI Powered ATS compatible resume generator
![ATScribe Cover Image](assets/cover_image.jpeg)


ATScribe is a command line tool that uses AI to generate ATS (Applicant Tracking System) compatible resumes. It leverages the power of LLM to create resumes that are optimized for ATS systems, ensuring that your resume gets noticed by recruiters and hiring managers.
## Features🚀
- AI Powered ATS compatible resume generator.

## Technology Stack🚀
- **Python 3.13**
- **[uv](https://docs.astral.sh/uv/)** package management
- **Langchain** for LLM and vector store integration
- **Gemini AI** for llm inference
- **Ollama** for running models locally

## How it works🚀
- Create your existing resume in PDF format.
- Create the job description in PDF format.
- Run the CLI tool and provide the paths to your resume and job description PDFs.

## Installation🚀
- - Install the `uv` package manager: https://docs.astral.sh/uv/getting-started/installation/
- Download the whl binary from the [releases page]()
- Add environment variables to your `.bashrc` or `.zshrc` file:
```text
`GEMINI_API_KEY`: Your Gemini API key, required if `USE_OLLAMA` is set to false.
`USE_OLLAMA`: Set to `true` if you want to use Ollama, otherwise set to `false`.
`MODEL_NAME`: The name of the model you want to use (e.g., `gemini-2.0-flash`).
```
- Setup a virtual environment:
```sh
uv venv --python 3.13.3
```
- Add the virtual environment to your .bashrc or .zshrc or equivalent shell configuration file:
```sh
source .venv/bin/activate
```
- Install the package using pip:
```sh
uv pip install atscribe-0.1.0-py3-none-any.whl
```
- Run the CLI tool:
```sh
atscribe path/to/resume.pdf path/to/job_description.pdf
```
---

- Clone the repository
- Setup `.env` file:
```sh
cp .env.example .env
```
- Edit the `.env` file to configure the following environment variables:
  - `GEMINI_API_KEY`: Your Gemini API key, required if `USE_OLLAMA` is set to false.
  - `USE_OLLAMA`: Set to `true` if you want to use Ollama, otherwise set to `false`.
  - `MODEL_NAME`: The name of the model you want to use (e.g., `gemini-2.0-flash`).
- Install the `uv` package manager: https://docs.astral.sh/uv/getting-started/installation/

- Install the package using `uv`:
```sh
uv sync
```
- Run the CLI tool:
```sh
bin/atscribe path/to/resume.pdf path/to/job_description.pdf
```
---
**To install globally, do the following steps:**
- Clone the repository
- Add the following to your `.bashrc` or `.zshrc` file to set up the environment:
```sh
export PATH=/PATH_TO_INSTALLATION/bin/:$PATH
```
- Run `atscribe` from the command line:
```sh
atscribe path/to/resume.pdf path/to/job_description.pdf
```
---
## Team🚀
> Our Contributors

<a href="https://github.com/vpk11/atscribe/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=vpk11/atscribe" />
</a>

---

## References🚀
- [Python 3.13 Documentation](https://docs.python.org/3.13/)
- [Langchain Documentation](https://python.langchain.com/docs/introduction/)
- [Gemini AI Documentation](https://ai.google.dev/gemini-api/docs)
- [uv Documentation](https://docs.astral.sh/uv/)
