# Use the official Miniconda base image
FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Copy the environment.yml and your application files into the container
COPY environment.yml .
COPY recommendation.py .
COPY app.py .
COPY start.sh .
COPY data ./data 
# Create the conda environment from the environment.yml
RUN conda env create -f environment.yml

# Make the script executable
RUN chmod +x start.sh

# Set the entry point to run the start script
CMD ["./start.sh"]

# Expose the port Streamlit will run on
EXPOSE 8501
