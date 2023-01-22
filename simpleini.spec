%global forgeurl https://github.com/brofield/simpleini

Version: 4.19

%forgemeta

Name: simpleini
Release: 2%{?dist}
Summary: Read and write INI-style configuration files.
URL:     %{forgeurl}
Source:  %{forgesource}
License: MIT

BuildRequires: gcc
BuildRequires: g++
BuildRequires: pkgconf-pkg-config
BuildRequires: gtest
BuildRequires: gtest-devel

%description
A cross-platform library that provides a simple API to read and write INI-style configuration files. It supports data files in ASCII, MBCS and Unicode. It is designed explicitly to be portable to any platform and has been tested
on Windows, WinCE and Linux. Released as open-source and free using the MIT licence.

%package libs
Summary: SimpleIni library files

%description libs
SimpleIni library files

%package devel
Summary: Files for development of applications which will use SimpleIni
Requires: %{name}-libs

%description devel
Files for development of applications which will use SimpleIni

%prep
%forgesetup

%build
gcc -g -Wall -shared -o libsimpleini.so -fPIC ConvertUTF.c

%install
mkdir -p %{buildroot}%{_includedir}/simpleini
mkdir -p %{buildroot}%{_libdir}/simpleini
install -C -m 644 SimpleIni.h %{buildroot}%{_includedir}/SimpleIni.h
install -C -m 644 ConvertUTF.h %{buildroot}%{_includedir}/ConvertUTF.h
install libsimpleini.so %{buildroot}%{_libdir}/libsimpleini.so

%check
cd tests
g++ -Wall -std=c++11 `pkg-config --cflags gtest_main` -c -o ts-roundtrip.o ts-roundtrip.cpp
g++ -Wall -std=c++11 `pkg-config --cflags gtest_main` -c -o ts-snippets.o ts-snippets.cpp
g++ -Wall -std=c++11 `pkg-config --cflags gtest_main` -c -o ts-utf8.o ts-utf8.cpp
g++ -Wall -std=c++11 `pkg-config --cflags gtest_main` -c -o ts-bugfix.o ts-bugfix.cpp
g++ -Wall -std=c++11 `pkg-config --cflags gtest_main` -c -o ts-quotes.o ts-quotes.cpp
g++ -Wall -std=c++11 `pkg-config --cflags gtest_main` -c -o ts-noconvert.o ts-noconvert.cpp
g++ -o ./tests ts-roundtrip.o ts-snippets.o ts-utf8.o ts-bugfix.o ts-quotes.o ts-noconvert.o `pkg-config --libs gtest_main`
./tests

%files
%license LICENCE.txt
%doc README.md

%files devel
%{_includedir}/SimpleIni.h
%{_includedir}/ConvertUTF.h

%files libs
%{_libdir}/libsimpleini.so

%changelog
* Sun Jan 22 2023 Leonardo Rossetti <lrossett@redhat.com> - 0.0.1-2
- Move header files /usr/include

* Sat Jan 21 2023 Leonardo Rossetti <lrossett@redhat.com> - 0.0.1
- First version being packaged
