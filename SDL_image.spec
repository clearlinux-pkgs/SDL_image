#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SDL_image
Version  : 1.2.12
Release  : 25
URL      : https://www.libsdl.org/projects/SDL_image/release/SDL_image-1.2.12.tar.gz
Source0  : https://www.libsdl.org/projects/SDL_image/release/SDL_image-1.2.12.tar.gz
Summary  : Simple DirectMedia Layer - Sample Image Loading Library
Group    : Development/Tools
License  : BSD-3-Clause IJG Libpng Zlib libtiff
Requires: SDL_image-lib = %{version}-%{release}
Requires: SDL_image-license = %{version}-%{release}
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(sdl)
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


%package lib
Summary: lib components for the SDL_image package.
Group: Libraries
Requires: SDL_image-license = %{version}-%{release}

%description lib
lib components for the SDL_image package.


%package license
Summary: license components for the SDL_image package.
Group: Default

%description license
license components for the SDL_image package.


%prep
%setup -q -n SDL_image-1.2.12
cd %{_builddir}/SDL_image-1.2.12
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664907452
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1664907452
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SDL_image
cp %{_builddir}/SDL_image-%{version}/COPYING %{buildroot}/usr/share/package-licenses/SDL_image/2aae6dd699d8e0d16b49d24a30009c7a3da2def8 || :
cp %{_builddir}/SDL_image-%{version}/VisualC/external/lib/x64/LICENSE.jpeg.txt %{buildroot}/usr/share/package-licenses/SDL_image/a71cd60ec9888ad7a814fa8ffa31e62cb0a84e4c || :
cp %{_builddir}/SDL_image-%{version}/VisualC/external/lib/x64/LICENSE.png.txt %{buildroot}/usr/share/package-licenses/SDL_image/fd071d8295b7ac1d4e235f5fa7d60fee3477efef || :
cp %{_builddir}/SDL_image-%{version}/VisualC/external/lib/x64/LICENSE.tiff.txt %{buildroot}/usr/share/package-licenses/SDL_image/023453b0b577b6ae8e7c2f7103bd53134a974605 || :
cp %{_builddir}/SDL_image-%{version}/VisualC/external/lib/x64/LICENSE.webp.txt %{buildroot}/usr/share/package-licenses/SDL_image/e46fe797dca4da720ef37e1f3f2d15f26b21f7d1 || :
cp %{_builddir}/SDL_image-%{version}/VisualC/external/lib/x64/LICENSE.zlib.txt %{buildroot}/usr/share/package-licenses/SDL_image/0aec4a494ca434e2d474b375e903d6c09da2a8fe || :
cp %{_builddir}/SDL_image-%{version}/VisualC/external/lib/x86/LICENSE.jpeg.txt %{buildroot}/usr/share/package-licenses/SDL_image/a71cd60ec9888ad7a814fa8ffa31e62cb0a84e4c || :
cp %{_builddir}/SDL_image-%{version}/VisualC/external/lib/x86/LICENSE.png.txt %{buildroot}/usr/share/package-licenses/SDL_image/fd071d8295b7ac1d4e235f5fa7d60fee3477efef || :
cp %{_builddir}/SDL_image-%{version}/VisualC/external/lib/x86/LICENSE.tiff.txt %{buildroot}/usr/share/package-licenses/SDL_image/023453b0b577b6ae8e7c2f7103bd53134a974605 || :
cp %{_builddir}/SDL_image-%{version}/VisualC/external/lib/x86/LICENSE.webp.txt %{buildroot}/usr/share/package-licenses/SDL_image/e46fe797dca4da720ef37e1f3f2d15f26b21f7d1 || :
cp %{_builddir}/SDL_image-%{version}/VisualC/external/lib/x86/LICENSE.zlib.txt %{buildroot}/usr/share/package-licenses/SDL_image/0aec4a494ca434e2d474b375e903d6c09da2a8fe || :
cp %{_builddir}/SDL_image-%{version}/Xcode/Frameworks/webp.framework/LICENSE.webp.txt %{buildroot}/usr/share/package-licenses/SDL_image/ff9a03d09711ea3f630767985780e5b279f45dd8 || :
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/SDL/SDL_image.h
/usr/lib64/libSDL_image.so
/usr/lib64/pkgconfig/SDL_image.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL_image-1.2.so.0
/usr/lib64/libSDL_image-1.2.so.0.8.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SDL_image/023453b0b577b6ae8e7c2f7103bd53134a974605
/usr/share/package-licenses/SDL_image/0aec4a494ca434e2d474b375e903d6c09da2a8fe
/usr/share/package-licenses/SDL_image/2aae6dd699d8e0d16b49d24a30009c7a3da2def8
/usr/share/package-licenses/SDL_image/a71cd60ec9888ad7a814fa8ffa31e62cb0a84e4c
/usr/share/package-licenses/SDL_image/e46fe797dca4da720ef37e1f3f2d15f26b21f7d1
/usr/share/package-licenses/SDL_image/fd071d8295b7ac1d4e235f5fa7d60fee3477efef
/usr/share/package-licenses/SDL_image/ff9a03d09711ea3f630767985780e5b279f45dd8
