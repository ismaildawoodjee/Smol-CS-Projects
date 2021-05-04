"""This script automates the downloading process of videos from 
DataCamp without having to resort to scraping and getting
blocked by hCaptcha. Of course I cannot do any work on my computer
while it is running, so best to leave it running overnight."""

import pyautogui as pag

BASE_URL = "https://campus.datacamp.com/courses/"

# Data Engineering with Python track
DE_URL_LIST = [
    "data-engineering-for-everyone",
    "introduction-to-data-engineering",
    "streamlined-data-ingestion-with-pandas",
    "writing-efficient-python-code",
    "writing-functions-in-python",
    "introduction-to-shell",
    "data-processing-in-shell",
    "introduction-to-bash-scripting",
    "unit-testing-for-data-science-in-python",
    "object-oriented-programming-in-python",
    "introduction-to-airflow-in-python",
    "introduction-to-pyspark",
    "building-data-engineering-pipelines-in-python",
    "introduction-to-aws-boto-in-python",
    "introduction-to-relational-databases-in-sql",
    "database-design",
    "introduction-to-scala",
    "big-data-fundamentals-with-pyspark",
    "cleaning-data-with-pyspark",
    "introduction-to-spark-sql-in-python",
    "cleaning-data-in-sql-server-databases",
    "transactions-and-error-handling-in-sql-server",
    "building-and-optimizing-triggers-in-sql-server",
    "improving-query-performance-in-sql-server",
    "introduction-to-using-mongodb-for-data-science-with-python"
]

DE_PAGES_LIST = [32, 57, 53, 53, 46, 55, 46, 43, 55, 44, 55,
                 45, 52, 54, 45, 52, 46, 55, 53, 52, 48, 52, 49, 58, 60]

# Data Analyst with SQL Server track
SQL_URL_LIST = [
    "introduction-to-sql-server",
    "introduction-to-relational-databases-in-sql",
    "intermediate-t-sql",
    "time-series-analysis-in-sql-server",
    "functions-for-manipulating-data-in-sql-server",
    "database-design",
    "hierarchical-and-recursive-queries-in-sql-server",
    "transactions-and-error-handling-in-sql-server",
    "writing-functions-and-stored-procedures-in-sql-server",
    "building-and-optimizing-triggers-in-sql-server",
    "improving-query-performance-in-sql-server"
]

SQL_PAGES_LIST = [
    46, 45, 47, 60, 54, 52, 47, 52, 57, 49, 58
]

# mixed Python Programmer and ML Scientist tracks (missed conda-essentials)
PP_URL_LIST = [
    "working-with-dates-and-times-in-python",
    "regular-expressions-in-python",
    "web-scraping-with-python",
    "software-engineering-for-data-scientists-in-python",
    "dimensionality-reduction-in-python",
    "hyperparameter-tuning-in-python",
    "winning-a-kaggle-competition-in-python",
    "machine-learning-with-tree-based-models-in-python",
    "cluster-analysis-in-python",
    "machine-learning-for-time-series-data-in-python",
    "feature-engineering-for-nlp-in-python",
    "introduction-to-tensorflow-in-python",
    "introduction-to-deep-learning-with-keras",
    "image-processing-in-python",
]

PP_PAGES_LIST = [
    48, 54, 56, 51, 58, 44, 52, 57, 46, 53, 52, 51, 59, 54
]

# with -61 download button offset
# PP_URL_LIST = [
#     "extreme-gradient-boosting-with-xgboost",
#     "preprocessing-for-machine-learning-in-python",
#     "feature-engineering-for-machine-learning-in-python",
#     "model-validation-in-python",
# ]

# for use with download button offset (last three Keras modules skipped)
PP0_URL_LIST = [
    "supervised-learning-with-scikit-learn",
    "unsupervised-learning-in-python",
    "linear-classifiers-in-python",
    "introduction-to-natural-language-processing-in-python",
    "introduction-to-deep-learning-in-python",
    "advanced-deep-learning-with-keras",
    "image-processing-with-keras-in-python"
]

# PP0_PAGES_LIST = [
#     49, 62, 53, 47, 54, 52, 44, 51, 50, 46, 45
# ]

PP0_PAGES_LIST = [
    54, 52, 44, 51, 50, 46, 45
]

ADDRESS_BAR = pag.Point(959, 65)
PLAY_BUTTON = pag.Point(996, 593)
DOWNLOAD_BUTTON = pag.Point(1383, 894)
DOWNLOAD_BUTTON0 = pag.Point(1383-61, 894)  # download button with offset
GO_NEXT_BUTTON = pag.Point(1125, 150)


def go_to_url(i, url_list, pages_list):
    """Uses PAG to go to specified URL in list"""
    print(
        f"Going to URL {i}: {url_list[i]}, with {pages_list[i]} pages"
    )
    pag.moveTo(ADDRESS_BAR, duration=0.5)
    pag.leftClick(ADDRESS_BAR)
    pag.write(BASE_URL + url_list[i], interval=0.01)
    pag.press("return")
    pag.sleep(10)


def check_video(page_id):
    """Uses the play_button image to check if there is video on page"""
    pag.sleep(8)
    pb = pag.locateOnScreen('play_button.png')
    if pb is not None:
        print(f"Play button found on Page {page_id}")
        return True
    else:
        print(f"Play button not found on Page {page_id}")
        return False


def download_video(video_exists, page_id, download_button):
    """Clicks Play and Download buttons in succession"""
    if video_exists:
        pag.moveTo(PLAY_BUTTON, duration=0.5)
        pag.leftClick(PLAY_BUTTON)
        pag.sleep(2)
        pag.moveTo(download_button, duration=0.5)
        pag.leftClick(download_button)
        print(f"Downloading video from Page {page_id}")
        return True
    return False


def save_video(proceed_saving, video_id):
    """Wait for video download box to appear before saving"""
    if proceed_saving:
        while not pag.getWindowsWithTitle("Opening"):
            pag.sleep(0.5)
        pag.sleep(3)
        pag.press("return")
        print(f"Video {video_id} saved")
    print("No video to save")


def go_next(video_exists, page_id):
    """Goes to next page"""
    if video_exists:
        print(f"Finished downloading video on Page {page_id}. Going next.\n")
    else:
        print(f"No video on Page {page_id}. Going next.\n")
    pag.moveTo(GO_NEXT_BUTTON, duration=0.5)
    pag.leftClick(GO_NEXT_BUTTON)
    pag.sleep(5)


def main(url_list, pages_list, db):
    """Loops over all URLs and pages in each module of a track""" 
    for (i, j) in zip(range(len(url_list)), pages_list):
        go_to_url(i, url_list=url_list, pages_list=pages_list)
        video_id = 0
        for p in range(j):
            video_exists = check_video(page_id=p)
            if video_exists:
                video_id += 1
                proceed_saving = download_video(
                    video_exists=video_exists, page_id=p, download_button=db
                )
                save_video(proceed_saving=proceed_saving, video_id=video_id)
            go_next(video_exists=video_exists, page_id=p)


if __name__ == "__main__":
    # approx 20 minutes per module in each track, longer depending on video quality
    main(url_list=PP_URL_LIST, pages_list=PP_PAGES_LIST, db=DOWNLOAD_BUTTON)
    main(url_list=PP0_URL_LIST, pages_list=PP0_PAGES_LIST, db=DOWNLOAD_BUTTON0)
