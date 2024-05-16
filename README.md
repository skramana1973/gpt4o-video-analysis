# gpt4o-video-analysis

### STEP 01- Create a conda environment after opening the repository

```bash
#conda create -n gpt4o-video-analysis python=3.10 -y
conda create -n gpt4o-video-analysis python=3.11.7 -y
```

```bash
conda activate gpt4o-video-analysis
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 04- copy any video file into data directory and change file name accordingly to match with code.

```bash
data/sample_video.mp4
```

### STEP 05- Finally run the following command

```bash
python gpt4o-vision-video-analysis.py
```