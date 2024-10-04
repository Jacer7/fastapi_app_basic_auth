# Use the AWS Lambda Python 3.11 base image
FROM public.ecr.aws/lambda/python:3.11

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy the rest of the application files to the Lambda task root
COPY . "${LAMBDA_TASK_ROOT}"

# Specify the Lambda handler (Mangum adapter)
CMD ["main.lambda_handler"]
