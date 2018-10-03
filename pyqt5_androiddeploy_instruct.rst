**Project** **Title**

PyqtDeploy

Getting Started:

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

**Prerequisites**:

1. There will PyQt5, pyqtdeploy, Android Studio, Apache, NDK, SDK, python, Java and QTCreator installed

    **PyQt5**: pip3 install PyQt5

    **pyqtdeploy**: pip3 install pyqtdeploy

    **python**: python version 3.6.4

    **Java**: sudo apt-get install openjdk-8-jdk

    **QTCreator**: QTCreator version 5.10.0

	- wget http://download.qt.io/official_releases/qt/5.10/5.10.0/qt-opensource-linux-x64-5.10.0.run

	-  chmod +x qt-opensource-linux-x64-5.10.0.run

	- ./qt-opensource-linux-x64-5.7.0.run

    **Apache**: apache verion apache-ant-1.10.5

	- wget http://mirror.its.dal.ca/apache//ant/binaries/apache-ant-1.10.5-bin.tar.gz

	- sudo tar -xf apache-ant-1.10.5-bin.tar.gz  -C /usr/local
	
	- sudo ln -s /usr/local/apache-ant-1.10.3/ /usr/local/ant 

    **Android** **Studio**: You can install Android Studio from: "https://developer.android.com/studio/"

    **NDK**: NDK version android-ndk-r10e

    **SDK**: You can configure the SDK from Android Studio

2. Configure the bashfile for export all relavent path. Like:

	export ANDROID_HOME=/opt/android/sdk

	export PATH=$PATH:/opt/android/sdk/platforms

	export PATH=$PATH:/opt/android/sdk/platforms-tools

	export PATH=$PATH:/opt/android/sdk/build-tools

	export PATH=$PATH:/opt/android/sdk/tools

	export PATH=$PATH:/home/cis/Documents/android-ndk-r10e

	export ANT_HOME=/home/cis/apache-ant-1.10.5

	export PATH=$PATH:/home/cis/apache-ant-1.10.5/bin

	export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

	export PATH=$PATH:$ANDROID_HOME/tools:apache-ant-1.10.5/bin/ant/bin:$JAVA_HOME/bin 

	export JAVA_OPTS='-XX:+IgnoreUnrecognizedVMOptions --add-modules java.se.ee'

	export ANDROID_NDK_ROOT=/home/cis/Documents/android-ndk-r10e

	export ANDROID_NDK_PLATFORM="android-21"

	export ANDROID_TOOLCHAIN=/home/cis/Documents/android-ndk-r10e/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/bin/

	export ANDROID_NDK_TOOLCHAIN_VERSION='4.9'

	export SYSROOT=/home/cis/Qt5.10.0/5.10.0/android_armv7


**Installing**

1. You need to install the pyqtdeploy tar package from the below link:

  "https://pypi.org/project/pyqtdeploy/#files" and untar the package.

2. Then you need to install the below tar files and need to place these tar files inside the "demo" folder of pyqtdeploy (which you have untar above)
	1. openssl-1.0.2n.tar.gz
	2. PyQt3D_gpl-5.10.1.tar.gz
	3. PyQt5_gpl-5.10.1.tar.gz
	4. PyQtChart_gpl-5.10.1.tar.gz
	5. PyQtDataVisualization_gpl-5.10.1.tar.gz
	6. PyQtPurchasing_gpl-5.10.1.tar.gz
	7. Python-3.6.4.tar.xz
	8. QScintilla_gpl-2.10.7.tar.xz
	9. sip-4.19.8.tar.gz

	most of the tar files will get from : "https://sourceforge.net/projects/pyqt/files/"

3. Then you need to also place "android_armv7" this folder inside the "demo" folder of pyqtdeploy.You will get android_armv7 from QTCreator folder which will install earlier(Qt5.10.0/5.10.0/android_armv7)

4. You also need to change the pyqt-demo.pdy file. To make changes in it run command "pyqtdeploy pyqt-demo.pdy" this will open a window in which we need to change the python to which we are using and in Standard Library section you need to check the xmlrpc, json, base64 and ssl and then save it.

5. Then you need to copy the SDK folder which is configured earlier to the root of system in opt folder the folder.Structure will be /opt/android/sdk/ and you also need to give permission to android folder recursively, so that all inner folders get permission as well.

**Deployment**

After all the installation and setup, need to run the command where the build-demo.py file is kept.

The command is: 

python3 build-demo.py --target android-32 --installed-qt-dir <Path to the installed directory of QT Creator>(/home/cis/Qt5.10.0/5.10.0)
