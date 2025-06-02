import argparse
import uuid
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.constants import START
from langgraph.graph import StateGraph, MessagesState
from pypdf import PdfReader
from rich.console import Console
from rich.markdown import Markdown
from yaspin import yaspin
from services.message_persistence_service import MessagePersistenceService


class Atscribe:
    @staticmethod
    def ask():
        session_id = uuid.uuid4()
        config = {"configurable": {"session_id": session_id}}
        builder = StateGraph(state_schema=MessagesState)
        builder.add_edge(START, "model")
        builder.add_node("model", MessagePersistenceService().call_model)
        graph = builder.compile()

        parser = argparse.ArgumentParser(description='Ask AI to generate resume based on the job description')
        parser.add_argument('resume', type=str, help='Path to the resume PDF file')
        parser.add_argument('job_desc', type=str, help='Path to the job description PDF file')
        args = parser.parse_args()

        with yaspin(text="Extracting content from resume and job description", color="yellow") as spinner:
            resume_content, job_desc_content = Atscribe.parse_pdfs(args)
            if resume_content == "" or job_desc_content == "":
                spinner.fail("❌ Failed:")
                return
            spinner.ok("📥")
        with yaspin(text="Generating ATS compatible resume", color="yellow") as spinner:
            input_message = Atscribe.construct_human_message(resume_content, job_desc_content)
            for event in graph.stream({"messages": [input_message]}, config, stream_mode="values"):
                last_message = event["messages"][-1]
                if isinstance(last_message, AIMessage):
                    console = Console()
                    md = Markdown(last_message.content)
                    spinner.ok("📝")
                    console.print(md)

    @staticmethod
    def construct_human_message(resume_content, job_desc_content):
        return HumanMessage(
            content=f"Resume Content:\n{resume_content}\n\nJob Description Content:\n{job_desc_content}"
        )

    @staticmethod
    def parse_pdfs(args):
        resume_text = ""
        job_desc_text = ""
        try:
            with open(args.resume, 'rb') as resume_file:
                reader = PdfReader(resume_file)
                resume_text = " ".join(page.extract_text() for page in reader.pages)

            with open(args.job_desc, 'rb') as job_file:
                reader = PdfReader(job_file)
                job_desc_text = " ".join(page.extract_text() for page in reader.pages)
            return resume_text, job_desc_text
        except Exception as _:
            return resume_text, job_desc_text