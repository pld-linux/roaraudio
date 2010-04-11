# TODO
# - see HACKING for packaging suggestions
# - libroar/libroar-devel should be complete, rest needs more work
# - figure out which libs go where
# - figure out which are drivers and which are compat
# - drop all the compat stuff?
# - roarmonhttp as subpackage (cgi/inetd server)
#
# Conditional build:
%bcond_with		arts        # with arts audio output
%bcond_without	esd     	# disable EsounD sound support
%bcond_without	nas     	# without NAS audio output
%bcond_without	pulseaudio  # without pulseaudio output
%bcond_without	sndfile		# without sndfile output
%bcond_without	yiff		# ...
%bcond_without	xmms		# don't build XMMS plugin
%bcond_without	audacious	# without audacious player support module

# celt version required for roaraudio
%define celt_release 0.7.1

%define		subver	beta4
%define		rel		0.1
Summary:	RoarAudio is a cross-platform sound system for both, home and professional use
Name:		roaraudio
Version:	0.3
Release:	0.%{subver}.%{rel}
License:	GPL v3, LGPL v3
Group:		Libraries
URL:		http://roaraudio.keep-cool.org/
Source0:	http://roaraudio.keep-cool.org/dl/%{name}-%{version}%{subver}.tar.gz
# Source0-md5:	001e5d9ecc65d80e14486d5157eb5d42
%{?with_arts:BuildRequires:	arts-devel}
%{?with_audacious:BuildRequires: audacious-devel}
#BuildRequires:	celt-devel >= %{celt_release}
%{?with_esd:BuildRequires:	esound-devel}
BuildRequires:	libao-devel
BuildRequires:	libdnet-devel
BuildRequires:	libfishsound-devel
%{?with_fishsound:BuildRequires:	libfishsound-devel}
BuildRequires:	libogg-devel
BuildRequires:	liboggz-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libshout-devel
%{?with_sndfile:BuildRequires:	libsndfile-devel}
BuildRequires:	libvorbis-devel
BuildRequires:	openslp-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	speex-devel >= 1:1.2
%{?with_xmms:BuildRequires:	xmms-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RoarAudio is a server for audio mixing. It's main purpose is to mix
audio from different clients before sending it to it's outputs. Those
outputs may for example be soundcards. It also supports network
clients because of it's full network transparency.

%package -n libroar
Summary:	RoarAudio sound system shared libraries
Group:		Libraries
Requires:	celt >= %{celt_release}

%description -n libroar
This package contains the shared libraries for the RoarAudio sound
system.

%package -n libroar-devel
Summary:	RoarAudio sound system header files and libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libroar-devel
This package contains static libraries and header files needed to
develop applications that use the RoarAudio sound system.

%package server
Summary:	RoarAudio sound system server daemon
Group:		Daemons
# roaraudio may call binaries which should be installed
Requires:	celt >= %{celt_release}
Requires:	flac
Requires:	vorbis-tools

%description server
This package contains the server daemon and related files for the
RoarAudio sound system.

%package utils
Summary:	RoarAudio sound system utilities
Group:		Applications/Multimedia
# roaraudio may call binaries which should be installed
Requires:	celt >= %{celt_release}
Requires:	gnuplot

%description utils
This package contains command line utilities for the RoarAudio sound
system.

%package -n xmms-output-roar
Summary:	RoarAudio sound system plugin for the XMMS
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libao

%description -n xmms-output-roar
This package contains the XMMS sound system plugin for the Audio
Output Library.

%package -n audacious-output-roar
Summary:	RoarAudio sound system plugin for the Audacious Media Player
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libao

%description -n audacious-output-roar
This package contains the Audacious Media Player sound system plugin
for the Audio Output Library.

%package -n libao-roar
Summary:	RoarAudio sound system plugin for the Audio Output Library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libao

%description -n libao-roar
This package contains the RoarAudio sound system plugin for the Audio
Output Library.

%package compat-esound
Summary:	RoarAudio sound system compatibility system for EsounD
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description compat-esound
This package contains the EsounD compatibility system for the
RoarAudio sound system.

%package compat-arts
Summary:	RoarAudio sound system compatibility system for aRts
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description compat-arts
This package contains the aRts compatibility system for the RoarAudio
sound system.

%package compat-nas
Summary:	RoarAudio sound system compatibility system for NAS
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description compat-nas
This package contains the NAS compatibility system for the RoarAudio
sound system.

%package compat-pulseaudio
Summary:	RoarAudio sound system compatibility system for PulseAudio
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description compat-pulseaudio
This package contains the PulseAudio compatibility system for the
RoarAudio sound system.

%package compat-sndfile
Summary:	RoarAudio sound system compatibility system for sndfile
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description compat-sndfile
This package contains the sndfile compatibility system for the
RoarAudio sound system.

%prep
%setup -q -n %{name}-%{version}%{subver}

find -name Makefile | xargs grep -l -- '-g -Wall -O2' | xargs sed -i -e 's,-g -Wall -O2,%{rpmcflags},'

sed -i -e '
	%{!?with_alsa:/libroarartsc.so/d}
	%{!?with_esd:/libroaresd.so/d}
	%{!?with_pulseaudio:/libroarpulse.so/d}
	%{!?with_sndfile:/libroarsndio.so/d}
	%{!?with_yiff:/libroaryiff.so/d}
	%{!?with_oss:/libroaross.so/d}
' symlinks.comp

%build
# NOTE: not autoconf derivered configure
./configure \
	--cc "%{__cc}" \
	--prefix %{_prefix} \
	--prefix-lib %{_libdir} \
	--prefix-comp-bins %{_bindir} \
	--prefix-comp-libs %{_libdir} \
	%{!?with_arts:--no-artsc} \
	%{!?with_xmms:--disable-xmms} \
	%{!?with_audacious:--without-audacious} \
	--runtime-detect \
	--cdrom /dev/cdrom \
	--tty /dev/tty \
	--oss-dev /dev/dsp

%{__make} \
	%{!?with_esd:TARGETS_ESD=} \
	%{!?with_arts:TARGETS_ARTS=} \
	%{!?with_nas:TARGETS_NAS=} \
	%{!?with_yiff:TARGETS_YIFF=} \
	%{!?with_pulseaudio:TARGETS_PA=}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# created by ldconfig
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.0.3

# make symlinks relative
for lib in $RPM_BUILD_ROOT%{_libdir}/lib*.so*; do
	[ -L $lib ] || continue
	target=$(readlink -f $lib)
	ln -snf $(basename $target) $lib
done

# remove non header files
rm -vf $RPM_BUILD_ROOT%{_includedir}/*/*.h.*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n libroar -p /sbin/ldconfig
%postun	-n libroar -p /sbin/ldconfig

%post	compat-esound -p /sbin/ldconfig
%postun	compat-esound -p /sbin/ldconfig

%post	compat-arts -p /sbin/ldconfig
%postun	compat-arts -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING README TODO
%attr(755,root,root) %{_bindir}/roarbidir
%attr(755,root,root) %{_bindir}/roarcat*
%attr(755,root,root) %{_bindir}/roarctl
%attr(755,root,root) %{_bindir}/roarfish
%attr(755,root,root) %{_bindir}/roarify
%attr(755,root,root) %{_bindir}/roarinterconnect
%attr(755,root,root) %{_bindir}/roarlight
%attr(755,root,root) %{_bindir}/roarmon*
%attr(755,root,root) %{_bindir}/roarradio
%attr(755,root,root) %{_bindir}/roarshout
%attr(755,root,root) %{_bindir}/roarsockconnect
%attr(755,root,root) %{_bindir}/roarsocktypes
%attr(755,root,root) %{_bindir}/roartypes
%attr(755,root,root) %{_bindir}/roarvorbis
%{_mandir}/man1/roarbaseclients.1*
%{_mandir}/man1/roarbidir.1*
%{_mandir}/man1/roarcat*.1*
%{_mandir}/man1/roarctl.1*
%{_mandir}/man1/roarfish.1*
%{_mandir}/man1/roarify.1*
%{_mandir}/man1/roarinterconnect.1*
%{_mandir}/man1/roarlight.1*
%{_mandir}/man1/roarmon.1*
%{_mandir}/man1/roarradio.1*
%{_mandir}/man1/roarshout.1*
%{_mandir}/man1/roarsockconnect.1*
%{_mandir}/man1/roarsocktypes.1*
%{_mandir}/man1/roartestclients.1*
%{_mandir}/man1/roartypes.1*
%{_mandir}/man1/roarvorbis.1*
%{_mandir}/man7/*.7*

%attr(755,root,root) %{_bindir}/yiff
%attr(755,root,root) %{_bindir}/yplay
%attr(755,root,root) %{_bindir}/yshutdown
%attr(755,root,root) %{_libdir}/libroaross.so
%attr(755,root,root) %ghost %{_libdir}/libroaross.so.0
%attr(755,root,root) %{_libdir}/libroaross.so.*.*.*

%files -n libroar
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libroar.so.0
%attr(755,root,root) %{_libdir}/libroar.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libroardsp.so.0
%attr(755,root,root) %{_libdir}/libroardsp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libroarmidi.so.0
%attr(755,root,root) %{_libdir}/libroarmidi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libroarlight.so.0
%attr(755,root,root) %{_libdir}/libroarlight.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libroareio.so.0
%attr(755,root,root) %{_libdir}/libroareio.so.*.*.*

%files -n libroar-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/roar-config
%{_includedir}/libroar
%{_includedir}/libroardsp
%{_includedir}/libroareio
%{_includedir}/libroaresd
%{_includedir}/libroarlight
%{_includedir}/libroarmidi
%{_includedir}/libroarpulse
%{_includedir}/libroarsndio
%{_includedir}/libroaryiff
%{_includedir}/roaraudio.h
%{_includedir}/roaraudio
%{_mandir}/man1/roar-config.1*
%{_mandir}/man3/*.3*
%{_libdir}/libroar.so
%{_libdir}/libroardsp.so
%{_libdir}/libroarmidi.so
%{_libdir}/libroarlight.so
%{_libdir}/libroareio.so

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/roard
%{_mandir}/man1/roarmonhttp.1*
%{_mandir}/man1/roard.1*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/roarfctest
%attr(755,root,root) %{_bindir}/roarfilt
%attr(755,root,root) %{_bindir}/roarsin
%attr(755,root,root) %{_bindir}/roarvumeter
%attr(755,root,root) %{_bindir}/roarphone
%{_mandir}/man1/roarfilt.1*
%{_mandir}/man1/roarphone.1*
%{_mandir}/man1/roarsin.1*
%{_mandir}/man1/roarvumeter.1*

%if %{with audacious}
%files -n audacious-output-roar
%defattr(644,root,root,755)
%{_libdir}/audacious/Output/libroar.so
%endif

%if %{with xmms}
%files -n xmms-output-roar
%defattr(644,root,root,755)
%attr(755,root,root) %{xmms_output_plugindir}/libroar.so
%endif

%files compat-esound
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/esd
%attr(755,root,root) %{_bindir}/esdcat
%attr(755,root,root) %{_bindir}/esdfilt
%attr(755,root,root) %{_bindir}/esdmon
%attr(755,root,root) %{_bindir}/esdplay
%attr(755,root,root) %ghost %{_libdir}/libroaresd.so.0
%attr(755,root,root) %{_libdir}/libroaresd.so.*.*.*

# compat libs pointing to libroaresd
%attr(755,root,root) %{_libdir}/libesd.so.0
# needed?
%attr(755,root,root) %{_libdir}/libroaresd.so
%attr(755,root,root) %{_libdir}/libesd.so
%attr(755,root,root) %{_libdir}/libesd.so.0.2
%attr(755,root,root) %{_libdir}/libesd.so.0.2.36

%if %{with arts}
%files compat-arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artscat
%attr(755,root,root) %{_bindir}/artsd
%attr(755,root,root) %{_bindir}/artsplay
%attr(755,root,root) %{_libdir}/libroarartsc.so
# compat libs pointing to libroarpulse
%attr(755,root,root) %{_libdir}/libartsc.so.0
# needed?
%attr(755,root,root) %{_libdir}/libartsc.so
%attr(755,root,root) %{_libdir}/libartsc.so.0.0
%attr(755,root,root) %{_libdir}/libartsc.so.0.0.0
%endif

%files compat-nas
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/auplay

%files compat-pulseaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pacat
%attr(755,root,root) %{_bindir}/paplay
%attr(755,root,root) %{_libdir}/libroarpulse.so
%attr(755,root,root) %ghost %{_libdir}/libroarpulse.so.0
%attr(755,root,root) %{_libdir}/libroarpulse.so.*.*.*
# compat libs pointing to libroarpulse
%attr(755,root,root) %{_libdir}/libpulse-simple.so.0
%attr(755,root,root) %{_libdir}/libpulse.so.0
# needed?
%attr(755,root,root) %{_libdir}/libpulse-simple.so
%attr(755,root,root) %{_libdir}/libpulse-simple.so.0.0
%attr(755,root,root) %{_libdir}/libpulse-simple.so.0.0.0
%attr(755,root,root) %{_libdir}/libpulse-simple.so.0.0.1
%attr(755,root,root) %{_libdir}/libpulse.so
%attr(755,root,root) %{_libdir}/libpulse.so.0.1
%attr(755,root,root) %{_libdir}/libpulse.so.0.1.0
%attr(755,root,root) %{_libdir}/libpulse.so.0.4
%attr(755,root,root) %{_libdir}/libpulse.so.0.4.1

%files compat-sndfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libroarsndio.so
%attr(755,root,root) %ghost %{_libdir}/libroarsndio.so.0
%attr(755,root,root) %{_libdir}/libroarsndio.so.*.*.*
