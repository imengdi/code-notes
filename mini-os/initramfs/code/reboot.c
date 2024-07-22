#include <unistd.h>
#include <sys/reboot.h>

#define LINUX_REBOOT_CMD_POWER_OFF  0x4321fedc
#define	LINUX_REBOOT_CMD_KEXEC		  0x45584543

int main(int argc, char **argv) {
  sync();
  setuid(0);
  // reboot argument: RB_AUTOBOOT
  reboot(RB_AUTOBOOT);
  return 0;
}
