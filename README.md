# Code Notes Repo
Sync the course code with network

## Mini Linux bootup manual

* Compile the app to binary

```
$ cd mini-os/initramfs/code
$ ./build.sh
```

* Build the initramfs with the apps

```
$ cd ../..
$ make
```

* Run the Mini-OS with Qemu

```
$ make run
```

* Exit the Qemu `Ctrl + A` then press `X`
