#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SDL_image
Version  : 1.2.12
Release  : 22
URL      : https://www.libsdl.org/projects/SDL_image/release/SDL_image-1.2.12.tar.gz
Source0  : https://www.libsdl.org/projects/SDL_image/release/SDL_image-1.2.12.tar.gz
Summary  : Simple DirectMedia Layer - Sample Image Loading Library
Group    : Development/Tools
License  : BSD-3-Clause IJG Libpng Zlib libtiff
Requires: SDL_image-lib = %{version}-%{release}
Requires: SDL_image-license = %{version}-%{release}
BuildRequires : SDL-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libpng)
BuildRequires : pkgconfig(32libwebp)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libwebp)
Patch1: CVE-2018-3977.patch
Patch2: CVE-2019-13616.patch
Patch3: CVE-2019-7635.patch

%description
This is a simple library to load images of various formats as SDL surfaces.
This library supports BMP, PPM, PCX, GIF, JPEG, PNG, and TIFF formats.

%package dev
Summary: dev components for the SDL_image package.
Group: Development
Requires: SDL_image-lib = %{version}-%{release}
Provides: SDL_image-devel = %{version}-%{release}
Requires: SDL_image = %{version}-%{release}

%description dev
dev components for the SDL_image package.


%package dev32
Summary: dev32 components for the SDL_image package.
Group: Default
Requires: SDL_image-lib32 = %{version}-%{release}
Requires: SDL_image-dev = %{version}-%{release}

%description dev32
dev32 components for the SDL_image package.


%package lib
Summary: lib components for the SDL_image package.
Group: Libraries
Requires: SDL_image-license = %{version}-%{release}

%description lib
lib components for the SDL_image package.


%package lib32
Summary: lib32 components for the SDL_image package.
Group: Default
Requires: SDL_image-license = %{version}-%{release}

%description lib32
lib32 components for the SDL_image package.


%package license
Summary: license components for the SDL_image package.
Group: Default

%description license
license components for the SDL_image package.


%prep
%setup -q -n SDL_image-1.2.12
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a SDL_image-1.2.12 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568876803
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1568876803
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SDL_image
cp COPYING %{buildroot}/usr/share/package-licenses/SDL_image/COPYING
cp VisualC/external/lib/x64/LICENSE.jpeg.txt %{buildroot}/usr/share/package-licenses/SDL_image/VisualC_external_lib_x64_LICENSE.jpeg.txt
cp VisualC/external/lib/x64/LICENSE.png.txt %{buildroot}/usr/share/package-licenses/SDL_image/VisualC_external_lib_x64_LICENSE.png.txt
cp VisualC/external/lib/x64/LICENSE.tiff.txt %{buildroot}/usr/share/package-licenses/SDL_image/VisualC_external_lib_x64_LICENSE.tiff.txt
cp VisualC/external/lib/x64/LICENSE.webp.txt %{buildroot}/usr/share/package-licenses/SDL_image/VisualC_external_lib_x64_LICENSE.webp.txt
cp VisualC/external/lib/x64/LICENSE.zlib.txt %{buildroot}/usr/share/package-licenses/SDL_image/VisualC_external_lib_x64_LICENSE.zlib.txt
cp VisualC/external/lib/x86/LICENSE.jpeg.txt %{buildroot}/usr/share/package-licenses/SDL_image/VisualC_external_lib_x86_LICENSE.jpeg.txt
cp VisualC/external/lib/x86/LICENSE.png.txt %{buildroot}/usr/share/package-licenses/SDL_image/VisualC_external_lib_x86_LICENSE.png.txt
cp VisualC/external/lib/x86/LICENSE.tiff.txt %{buildroot}/usr/share/package-licenses/SDL_image/VisualC_external_lib_x86_LICENSE.tiff.txt
cp VisualC/external/lib/x86/LICENSE.webp.txt %{buildroot}/usr/share/package-licenses/SDL_image/VisualC_external_lib_x86_LICENSE.webp.txt
cp VisualC/external/lib/x86/LICENSE.zlib.txt %{buildroot}/usr/share/package-licenses/SDL_image/VisualC_external_lib_x86_LICENSE.zlib.txt
cp Xcode/Frameworks/webp.framework/LICENSE.webp.txt %{buildroot}/usr/share/package-licenses/SDL_image/Xcode_Frameworks_webp.framework_LICENSE.webp.txt
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/SDL/SDL_image.h
/usr/lib64/libSDL_image.so
/usr/lib64/pkgconfig/SDL_image.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libSDL_image.so
/usr/lib32/pkgconfig/32SDL_image.pc
/usr/lib32/pkgconfig/SDL_image.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL_image-1.2.so.0
/usr/lib64/libSDL_image-1.2.so.0.8.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libSDL_image-1.2.so.0
/usr/lib32/libSDL_image-1.2.so.0.8.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SDL_image/COPYING
/usr/share/package-licenses/SDL_image/VisualC_external_lib_x64_LICENSE.jpeg.txt
/usr/share/package-licenses/SDL_image/VisualC_external_lib_x64_LICENSE.png.txt
/usr/share/package-licenses/SDL_image/VisualC_external_lib_x64_LICENSE.tiff.txt
/usr/share/package-licenses/SDL_image/VisualC_external_lib_x64_LICENSE.webp.txt
/usr/share/package-licenses/SDL_image/VisualC_external_lib_x64_LICENSE.zlib.txt
/usr/share/package-licenses/SDL_image/VisualC_external_lib_x86_LICENSE.jpeg.txt
/usr/share/package-licenses/SDL_image/VisualC_external_lib_x86_LICENSE.png.txt
/usr/share/package-licenses/SDL_image/VisualC_external_lib_x86_LICENSE.tiff.txt
/usr/share/package-licenses/SDL_image/VisualC_external_lib_x86_LICENSE.webp.txt
/usr/share/package-licenses/SDL_image/VisualC_external_lib_x86_LICENSE.zlib.txt
/usr/share/package-licenses/SDL_image/Xcode_Frameworks_webp.framework_LICENSE.webp.txt
