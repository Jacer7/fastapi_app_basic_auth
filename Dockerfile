# Use the AWS Lambda Python 3.11 base image
FROM public.ecr.aws/lambda/python:3.11

# Copy the requirements file into the image
COPY requirements.txt ${LAMBDA_TASK_ROOT}/

# Install the Python dependencies directly into the Lambda task root
RUN pip install --upgrade pip && pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy the rest of your application files into the image
COPY . "${LAMBDA_TASK_ROOT}"

# Specify the Lambda handler (Mangum adapter)
CMD ["main.handler"]
