.PHONY: initramfs run clean

$(shell mkdir -p build)

initramfs: apps
	@cd initramfs && find . -print0 | cpio --null -ov --format=newc | gzip -9 \
	  > ../build/initramfs.cpio.gz

run:
	@qemu-system-x86_64 \
	  -nographic \
	  -serial mon:stdio \
	  -m 128 \
	  -kernel boot/Image \
	  -initrd build/initramfs.cpio.gz \
	  -append "console=ttyS0 quiet acpi=off"

clean:
	@rm -rf build
	@rm -rf initramfs/apps

apps:
	@./build-apps.sh
