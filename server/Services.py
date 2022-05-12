from string import Template
import os

def main(logger):
  ## Create the gdrive file
  rclone_config = {
    'uagent': 'z',
    'vfs_ll': 'NOTICE',
    'vfs_bs': '16M',
    'vfs_rcs': '64M',
    'vfs_rcsl': '1024M',
    'vfs_cm': 'writes',
    'vfs_cma': '1h',
    'vfs_cms': 'off',
    'vfs_dct': '5m',
    'vfs_t': '8',
    'vfs_mt': '750G',
    'vfs_c': '16'
  }

  CopyFiles('gdrive.service', '/etc/systemd/system/gdrive.service', logger, rclone_config)
  CopyFiles('gcrypt.service', '/etc/systemd/system/gcrypt.service', logger, rclone_config)
  CopyFiles('tcrypt.service', '/etc/systemd/system/tcrypt.service', logger, rclone_config)
  CopyFiles('tdrive.service', '/etc/systemd/system/tdrive.service', logger, rclone_config)


def CopyFiles(source, destination, logger, contents = {}):
  if os.path.isfile(destination):
    logger.warning("Skipping file, since it exists!: " + destination )
  else:
    logger.info("Creating file: " + destination )

    filepath = os.path.join('./templates', source)

    with open(filepath, 'r') as f:
      src = Template(f.read())
      result = src.substitute(contents)
      logger.debug(result)

    with open(destination, 'a') as f:
      f.write(result)
