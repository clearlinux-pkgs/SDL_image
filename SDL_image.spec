#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SDL_image
Version  : 1.2.12
Release  : 8
URL      : https://www.libsdl.org/projects/SDL_image/release/SDL_image-1.2.12.tar.gz
Source0  : https://www.libsdl.org/projects/SDL_image/release/SDL_image-1.2.12.tar.gz
Summary  : Simple DirectMedia Layer - Sample Image Loading Library
Group    : Development/Tools
License  : BSD-3-Clause IJG Libpng Zlib libtiff
Requires: SDL_image-lib
BuildRequires : SDL-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libwebp)

%description
This is a simple library to load images of various formats as SDL surfaces.
This library supports BMP, PPM, PCX, GIF, JPEG, PNG, and TIFF formats.

%package dev
Summary: dev components for the SDL_image package.
Group: Development
Requires: SDL_image-lib
Provides: SDL_image-devel

%description dev
dev components for the SDL_image package.


%package lib
Summary: lib components for the SDL_image package.
Group: Libraries

%description lib
lib components for the SDL_image package.


%prep
%setup -q -n SDL_image-1.2.12

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
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
