#
# Copyright (C) 2010 OpenWrt.org
#

PART_NAME=firmware
REQUIRE_IMAGE_METADATA=1

RAMFS_COPY_BIN='fw_printenv fw_setenv'
RAMFS_COPY_DATA='/etc/fw_env.config /var/lock/fw_printenv.lock'

platform_check_image() {
	return 0
}

platform_pre_upgrade() {
	:
}

platform_nand_pre_upgrade() {
	:
}

platform_do_upgrade() {
	default_do_upgrade "$1"
}
