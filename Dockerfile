# Use the AWS Lambda Python 3.11 base image
FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt requirements.txt
# Copy the requirements file and install dependencies

RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY . "${LAMBDA_TASK_ROOT}"
# Specify the Lambda handler (Mangum adapter)
CMD ["main.handler"]  
