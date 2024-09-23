# syl
Software and documentation for my smart home server.

## Hardware

* Raspberry Pi 5
* ReSpeaker 2-Mics Pi HAT

## Software

### Operating System

I used `Raspberry Pi Imager` to install the most recent version of the 64-bit Raspberry Pi OS.

> [!TIP]
> I expected SSH to work out-of-the-box, but unfortunately I had to connect my Pi up to
> a display and use the GUI to enable SSH service. I also enabled I2C and SPI service which
> may have been necessary for the `ReSpeaker 2-Mics Pi Hat`.


#### Kernel Version

```
uname -r
6.6.31+rpt-rpi-2712
```

### ReSpeaker 2-Mics Pi HAT

#### driver

> [!WARNING]
> The drivers are pretty finicky. I originally had a generic Ubuntu server OS installed and toiled for hours
> trying to get the drivers to work, and never succeeded. I finally decided to just try the default
> Raspberry Pi OS from `Raspberry Pi Imager` and that worked out of the box. I never tried the original
> `respeaker`'s repo of `seed-voicecard` as I read it does not support Raspberry Pi 5, and went straight
> for `HinTak`'s fork which worked without issue.

I installed the driver from the `HinTak` fork of `seeed-voicecard`: https://github.com/HinTak/seeed-voicecard

Specifically the `v6.6` branch which matches up with my kernel version.

Following the instructions worked without issue:

```
git clone https://github.com/HinTak/seeed-voicecard.git
cd seeed-voicecard
sudo ./ubuntu-prerequisite.sh
sudo ./install.sh
sudo reboot now
```

After that I could see my device:
```
arecord -l

**** List of CAPTURE Hardware Devices ****
card 0: Microphone [Yeti Stereo Microphone], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: seeed2micvoicec [seeed-2mic-voicecard], device 0: 1f000a0000.i2s-wm8960-hifi wm8960-hifi-0 [1f000a0000.i2s-wm8960-hifi wm8960-hifi-0]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

Recording and playback work fine:
```
[syl@syl] arecord --device="hw:1,0" -f S32_LE --rate 48000 -c 2 -d 5 hat.wav
[sean@DESKTOP] scp syl:~/hat.wav .

# Use media player to play file at:
# \\wsl.localhost\Ubuntu\home\sean\hat.wav
```
