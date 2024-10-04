# Use the AWS Lambda Python 3.11 base image
FROM public.ecr.aws/lambda/python:3.11

# Set the working directory in the container
WORKDIR /fastapi

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the rest of the FastAPI app files
COPY . .

# Specify the Lambda handler (Mangum adapter)
CMD ["main.lambda_handler"]  
