# Use the AWS Lambda Python 3.11 base image
FROM public.ecr.aws/lambda/python:3.11


COPY . $(LAMBDA_TASK_ROOT)
# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt - target "${LAMBDA_TASK_ROOT}" -U - no-cache-dir

# Specify the Lambda handler (Mangum adapter)
CMD ["main.handler"]  
