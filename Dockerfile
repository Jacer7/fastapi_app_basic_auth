FROM public.ecr.aws/lambda/python:3.11

# Install necessary system packages
RUN yum install -y gcc libffi-devel python3-devel openssl-devel

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY . "${LAMBDA_TASK_ROOT}"
CMD ["main.lambda_handler"]
