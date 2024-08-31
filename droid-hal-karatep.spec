# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device karatep
%define vendor lenovo

%define vendor_pretty Lenovo
%define device_pretty K6 Note

%define installable_zip 1

%define droid_target_aarch64 1

#define apex_path "system/apex/com.android.runtime"

%define straggler_files \
/bugreports\
/d\
/dsp\
/firmware\
/product\
/sdcard\
/system_ext\
%{nil}

%include rpm/dhd/droid-hal-device.inc


# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

