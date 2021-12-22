## **Media Encoder Shutdown** ##


### Features
---

 - This is a simple utility that shutdown the computer after Adobe Media Encoder finished processing.

 - Open the App when Media Encoder is processing your task list and when Media Encoder finishes, the app will wait a few minutes and then will shutdown the computer.

---

### Motivation

If you use Adobe Media Encoder to process your videos sometimes it takes lots of hours to finish. But since ME doesn't have an option to shutdown the computer, your computer will stayed powered on.

This tool helps with that, it monitors the Media Enconder's CPU usage and shuts down the computer a few minutes after ME finishes its work.

---
### Dependencies

This app relies on [psutil](https://pypi.org/project/psutil/) 

`
pip install psutil
`

The windows executable version, avaiable on releases was made with [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/)

`
pip install auto-py-to-exe
`


---
### Build
To build this I've used Python 3.6 (and tried with Pyton 3.10.1).  

---
### Download
Python file: [click here](https://github.com/DiegoDN/MediaEncoderShutdown/blob/master/src/MediaEncoderShutdown.py) 

Windows version: Download ZIP from releases [v1.0](https://github.com/DiegoDN/MediaEncoderShutdown/releases/download/1.0/Media.Encoder.Shutdown.zip)  or click [here](https://github.com/DiegoDN/MediaEncoderShutdown/releases/tag/1.0)

---
### How to Use
You can run the app from IDLE IDE + Run Module (hit F5 key), or use the converted windows version running *MediaEncoderShutdown.exe*

