import os

def CreateDir(logger, dir):
  if os.path.isdir(dir):
    logger.warning("Skipping directory, since it exists!: " + dir)
  else:
    logger.info("Creating directory: " + dir)
    os.mkdir(dir)
