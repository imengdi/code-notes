# Code Notes Repo
Sync the course code with network

## Mini Linux bootup manual

* Compile the app to binary

```
$ cd mini-os
$ make apps
```

* Build the initramfs with the apps included

```
$ make
```

* Run the mini Linux with Qemu

```
$ make run
```

* Run the apps in mini Linux

```
(linux)$ cd apps
(linux)$ ./hello
Hello, OS World
(linux)$ timeout 3 ./logisim
A = 1; B = 1; C = 1; D = 1; E = 1; F = 1; G = 0;
A = 0; B = 1; C = 1; D = 0; E = 0; F = 0; G = 0;
A = 1; B = 1; C = 0; D = 1; E = 1; F = 0; G = 1;
Terminated
```

* Exit the Qemu `Ctrl + A` then press `X`
