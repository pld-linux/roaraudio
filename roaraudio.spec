# TODO
# - RAUM (libraum, raum.h) [http://raum.keep-cool.org/, http://roaraudio.keep-cool.org/uniraum.html - not released yet]
# - libossaudio (OSS 4?)
# - PABLIO (libpablio, pablio/pablio.h)
# - see HACKING for packaging suggestions
# - libroar/libroar-devel should be complete, rest needs more work
# - figure out which libs go where
# - figure out which are drivers and which are compat
# - drop all the compat stuff?
# - roarmonhttp as subpackage (cgi/inetd server)
# NOTE:
# - -ldnet it searches is for DEC Networking, not our libdnet
#
# Conditional build:
%bcond_with	arts		# aRts audio output
%bcond_without	esd		# EsounD sound support
%bcond_without	nas		# NAS audio output
%bcond_without	oss		# OSS compatibility layer
%bcond_without	pulseaudio	# pulseaudio output
%bcond_without	rsound		# RSound support
%bcond_without	sndfile		# sndfile output
%bcond_without	yiff		# YIFF sound server support
%bcond_without	xmms		# XMMS plugin
%bcond_with	audacious	# audacious player plugin [temporarily(?) removed from sources]

# celt version required for roaraudio
%define		celt_ver 0.7.1

Summary:	RoarAudio is a cross-platform sound system for both, home and professional use
Summary(pl.UTF-8):	RoarAudio - wieloplatformowy system dźwięku do użytku domowego i profesjonalnego
Name:		roaraudio
Version:	0.4
Release:	0.1
License:	GPL v3, LGPL v3
Group:		Libraries
Source0:	http://roaraudio.keep-cool.org/dl/%{name}-%{version}.tar.gz
# Source0-md5:	74b5ea7805f7986954435cfb9917827e
Patch0:		%{name}-celt.patch
Patch1:		%{name}-flac.patch
Patch2:		%{name}-arts.patch
URL:		http://roaraudio.keep-cool.org/
BuildRequires:	alsa-lib-devel >= 0.9
%{?with_arts:BuildRequires:	artsc-devel}
%{?with_audacious:BuildRequires: audacious-devel}
BuildRequires:	celt-devel >= %{celt_ver}
BuildRequires:	dbus-devel
%{?with_esd:BuildRequires:	esound-devel}
BuildRequires:	flac-devel
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libao-devel
BuildRequires:	libfishsound-devel
%{?with_fishsound:BuildRequires:	libfishsound-devel}
BuildRequires:	libgcrypt-devel
BuildRequires:	libogg-devel
BuildRequires:	liboggz-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libshout-devel
%{?with_sndfile:BuildRequires:	libsndfile-devel}
BuildRequires:	libuuid-devel
BuildRequires:	libvorbis-devel
BuildRequires:	openslp-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel >= 19
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel}
BuildRequires:	sed >= 4.0
BuildRequires:	speex-devel >= 1:1.2
BuildRequires:	which
BuildRequires:	xorg-lib-libX11-devel
%{?with_xmms:BuildRequires:	xmms-devel}
%{?with_yiff:BuildRequires:	yiff-devel}
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RoarAudio is a server for audio mixing. It's main purpose is to mix
audio from different clients before sending it to it's outputs. Those
outputs may for example be soundcards. It also supports network
clients because of it's full network transparency.

%description -l pl.UTF-8
RoarAudio to serwer do miksowania dźwięku. Jego głównym celem jest
miksowanie dźwięku od różnych klientów przed przesłaniem go do wyjść.
Wyjścia mogą być na przykład kartami dźwiękowymi. Obsługiwani są także
klienci sieciowi, ponieważ serwer jest w pełni przezroczysty sieciowo.

%package -n libroar
Summary:	RoarAudio sound system shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone systemu dźwięku RoarAudio
Group:		Libraries
Requires:	celt >= %{celt_ver}

%description -n libroar
This package contains the shared libraries for the RoarAudio sound
system.

%description -n libroar -l pl.UTF-8
Ten pakiet zawiera biblioteki współdzielone systemu dźwięku RoarAudio.

%package -n libroar-devel
Summary:	RoarAudio sound system header files
Group:		Development/Libraries
Requires:	libroar = %{version}-%{release}

%description -n libroar-devel
This package contains the header files needed to develop applications
that use the RoarAudio sound system.

%description -n libroar-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe niezbędne do tworzenia aplikacji
wykorzystujących system dźwięku RoarAudio.

%package server
Summary:	RoarAudio sound system server daemon
Summary(pl.UTF-8):	Demon serwera systemu dźwięku RoarAudio
Group:		Daemons
# roaraudio may call binaries which should be installed
Requires:	celt >= %{celt_ver}
Requires:	flac
Requires:	vorbis-tools

%description server
This package contains the server daemon and related files for the
RoarAudio sound system.

%description server -l pl.UTF-8
Ten pakiet zawiera demona serwera oraz związane z nim pliki dla
systemu dźwięku RoarAudio.

%package utils
Summary:	RoarAudio sound system utilities
Summary(pl.UTF-8):	Narzędzia dla systemu dźwięku RoarAudio
Group:		Applications/Multimedia
# roaraudio may call binaries which should be installed
Requires:	celt >= %{celt_ver}
Requires:	gnuplot

%description utils
This package contains command line utilities for the RoarAudio sound
system.

%description utils -l pl.UTF-8
Ten pakiet zawiera narzędzia linii poleceń dla systemu dźwięku
RoarAudio.

%package compat-arts
Summary:	RoarAudio sound system compatibility system for aRts
Summary(pl.UTF-8):	Warstwa zgodności systemu dźwięku RoarAudio dla systemu aRts
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description compat-arts
This package contains the aRts compatibility system for the RoarAudio
sound system.

%description compat-arts -l pl.UTF-8
Ten pakiet zawiera warstwę zgodności systemu dźwięku RoarAudio dla
systemu aRts.

%package compat-esound
Summary:	RoarAudio sound system compatibility system for EsounD
Summary(pl.UTF-8):	Warstwa zgodności systemu dźwięku RoarAudio dla systemu EsounD
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description compat-esound
This package contains the EsounD compatibility system for the
RoarAudio sound system.

%description compat-esound -l pl.UTF-8
Ten pakiet zawiera warstwę zgodności systemu dźwięku RoarAudio dla
systemu EsounD.

%package compat-nas
Summary:	RoarAudio sound system compatibility system for NAS
Summary(pl.UTF-8):	Warstwa zgodności systemu dźwięku RoarAudio dla systemu NAS
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description compat-nas
This package contains the NAS compatibility system for the RoarAudio
sound system.

%description compat-nas -l pl.UTF-8
Ten pakiet zawiera warstwę zgodności systemu dźwięku RoarAudio dla
systemu NAS.

%package compat-oss
Summary:	RoarAudio sound system compatibility system for OSS
Summary(pl.UTF-8):	Warstwa zgodności systemu dźwięku RoarAudio dla systemu OSS
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description compat-oss
This package contains the OSS compatibility system for the RoarAudio
sound system.

%description compat-oss -l pl.UTF-8
Ten pakiet zawiera warstwę zgodności systemu dźwięku RoarAudio dla
systemu OSS.

%package compat-pulseaudio
Summary:	RoarAudio sound system compatibility system for PulseAudio
Summary(pl.UTF-8):	Warstwa zgodności systemu dźwięku RoarAudio dla systemu PulseAudio
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description compat-pulseaudio
This package contains the PulseAudio compatibility system for the
RoarAudio sound system.

%description compat-pulseaudio -l pl.UTF-8
Ten pakiet zawiera warstwę zgodności systemu dźwięku RoarAudio dla
systemu PulseAudio.

%package compat-rsound
Summary:	RoarAudio sound system compatibility system for RSound
Summary(pl.UTF-8):	Warstwa zgodności systemu dźwięku RoarAudio dla systemu RSound
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description compat-rsound
This package contains the RSound compatibility system for the
RoarAudio sound system.

%description compat-rsound -l pl.UTF-8
Ten pakiet zawiera warstwę zgodności systemu dźwięku RoarAudio dla
systemu RSound.

%package compat-sndfile
Summary:	RoarAudio sound system compatibility system for sndfile
Summary(pl.UTF-8):	Warstwa zgodności systemu dźwięku RoarAudio dla sndfile
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description compat-sndfile
This package contains the sndfile compatibility system for the
RoarAudio sound system.

%description compat-sndfile -l pl.UTF-8
Ten pakiet zawiera warstwę zgodności systemu dźwięku RoarAudio dla
sndfile.

%package compat-yiff
Summary:	RoarAudio sound system compatibility system for YIFF
Summary(pl.UTF-8):	Warstwa zgodności systemu dźwięku RoarAudio dla systemu YIFF
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description compat-yiff
This package contains the YIFF compatibility system for the RoarAudio
sound system.

%description compat-yiff -l pl.UTF-8
Ten pakiet zawiera warstwę zgodności systemu dźwięku RoarAudio dla
systemu YIFF.

%package -n libao-roar
Summary:	RoarAudio sound system plugin for the Audio Output Library
Summary(pl.UTF-8):	Wtyczka systemu dźwięku RoarAudio dla biblioteki Audio Output
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libao

%description -n libao-roar
This package contains the RoarAudio sound system plugin for the Audio
Output Library.

%description -n libao-roar -l pl.UTF-8
Ten pakiet zawiera wtyczkę systemu dźwięku RoarAudio dla biblioteki
Audio Output.

%package -n xmms-output-roar
Summary:	RoarAudio sound system plugin for XMMS
Summary(pl.UTF-8):	Wtyczka systemu dźwięku RoarAudio dla odtwarzacza XMMS
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xmms

%description -n xmms-output-roar
This package contains the RoarAudio sound system plugin for XMMS.

%description -n xmms-output-roar -l pl.UTF-8
Ten pakiet zawiera wtyczkę systemu dźwięku RoarAudio dla odtwarzacza
XMMS.

%package -n audacious-output-roar
Summary:	RoarAudio sound system plugin for the Audacious Media Player
Summary(pl.UTF-8):	Wtyczka systemu dźwięku RoarAudio dla odtwarzacza Audacious Media Player
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libao

%description -n audacious-output-roar
This package contains the Audacious Media Player sound system plugin
for the Audacious Media Player.

%description -n audacious-output-roar -l pl.UTF-8
Ten pakiet zawiera wtyczkę systemu dźwięku RoarAudio dla odtwarzacza
Audacious Media Player.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e '
	%{!?with_arts:/libroarartsc.so/d}
	%{!?with_esd:/libroaresd.so/d}
	%{!?with_pulseaudio:/libroarpulse.so/d}
	%{!?with_rsound:/libroarrsound.so/d}
	%{!?with_sndfile:/libroarsndio.so/d}
	%{!?with_yiff:/libroaryiff.so/d}
	%{!?with_oss:/libroaross.so/d}
' symlinks.comp

%build
# NOTE: not autoconf derivered configure
./configure \
	--cc "%{__cc}" \
	--cflags "%{rpmcflags} %{rpmcppflags}" \
	--ldflags "%{rpmldflags}" \
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
	%{!?with_rsound:TARGETS_RSOUND=} \
	%{!?with_yiff:TARGETS_YIFF=} \
	%{!?with_pulseaudio:TARGETS_PA=}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# make symlinks relative
for lib in $RPM_BUILD_ROOT%{_libdir}/lib*.so*; do
	[ -L $lib ] || continue
	target=$(readlink -f $lib)
	ln -snf $(basename $target) $lib
done

# old test programs, not installed now
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/{roarfctest,roarsocktypes}.1

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

%post	compat-pulseaudio -p /sbin/ldconfig
%postun	compat-pulseaudio -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING README TODO
%attr(755,root,root) %{_bindir}/dtmfdial
%attr(755,root,root) %{_bindir}/roarbidir
%attr(755,root,root) %{_bindir}/roarcat*
%attr(755,root,root) %{_bindir}/roarclientpass
%attr(755,root,root) %{_bindir}/roarctl
%attr(755,root,root) %{_bindir}/roardtmf
%attr(755,root,root) %{_bindir}/roarfish
%attr(755,root,root) %{_bindir}/roarify
%attr(755,root,root) %{_bindir}/roarinterconnect
%attr(755,root,root) %{_bindir}/roarlight
%attr(755,root,root) %{_bindir}/roarmon*
%attr(755,root,root) %{_bindir}/roarradio
%attr(755,root,root) %{_bindir}/roarshout
%attr(755,root,root) %{_bindir}/roarsockconnect
%attr(755,root,root) %{_bindir}/roartypes
%attr(755,root,root) %{_bindir}/roarvio
%attr(755,root,root) %{_bindir}/roarvorbis
%{_mandir}/man1/roarbaseclients.1*
%{_mandir}/man1/roarbidir.1*
%{_mandir}/man1/roarcat*.1*
%{_mandir}/man1/roarclientpass.1*
%{_mandir}/man1/roarctl.1*
%{_mandir}/man1/roardtmf.1*
%{_mandir}/man1/roarfish.1*
%{_mandir}/man1/roarify.1*
%{_mandir}/man1/roarinterconnect.1*
%{_mandir}/man1/roarlight.1*
%{_mandir}/man1/roarmon.1*
%{_mandir}/man1/roarradio.1*
%{_mandir}/man1/roarshout.1*
%{_mandir}/man1/roarsockconnect.1*
%{_mandir}/man1/roartestclients.1*
%{_mandir}/man1/roartypes.1*
%{_mandir}/man1/roarvio.1*
%{_mandir}/man1/roarvorbis.1*
%{_mandir}/man7/RoarAudio.7*
%{_mandir}/man7/roardecnet.7*
%{_mandir}/man7/roartips.7*

%files -n libroar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libroar.so.1
%attr(755,root,root) %{_libdir}/libroardsp.so.1
%attr(755,root,root) %{_libdir}/libroareio.so.1
%attr(755,root,root) %{_libdir}/libroarlight.so.1
%attr(755,root,root) %{_libdir}/libroarmidi.so.1

%files -n libroar-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/roar-config
%attr(755,root,root) %{_libdir}/libroar.so
%attr(755,root,root) %{_libdir}/libroardsp.so
%attr(755,root,root) %{_libdir}/libroarmidi.so
%attr(755,root,root) %{_libdir}/libroarlight.so
%attr(755,root,root) %{_libdir}/libroareio.so
%{_includedir}/libroar
%{_includedir}/libroardsp
%{_includedir}/libroareio
%{_includedir}/libroaresd
%{_includedir}/libroarlight
%{_includedir}/libroarmidi
%{_includedir}/libroarpulse
%{_includedir}/libroarsndio
%{_includedir}/libroarrsound
%{_includedir}/libroaryiff
%{_includedir}/roaraudio.h
%{_includedir}/roaraudio
%{_pkgconfigdir}/libroar.pc
%{_pkgconfigdir}/libroardsp.pc
%{_pkgconfigdir}/libroareio.pc
%{_pkgconfigdir}/libroarlight.pc
%{_pkgconfigdir}/libroarmidi.pc
%{_mandir}/man1/roar-config.1*
%{_mandir}/man3/roar_*.3*
%{_mandir}/man7/libroar.7*
%{_mandir}/man7/roartut.7*
%{_mandir}/man7/roarvio.7*
%{_mandir}/man7/roarvs.7*

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/roard
%{_mandir}/man1/roarmonhttp.1*
%{_mandir}/man1/roard.1*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/roarfilt
%attr(755,root,root) %{_bindir}/roarsin
%attr(755,root,root) %{_bindir}/roarvumeter
%attr(755,root,root) %{_bindir}/roarphone
%{_mandir}/man1/roarfilt.1*
%{_mandir}/man1/roarphone.1*
%{_mandir}/man1/roarsin.1*
%{_mandir}/man1/roarvumeter.1*

%if %{with arts}
%files compat-arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artscat
%attr(755,root,root) %{_bindir}/artsd
%attr(755,root,root) %{_bindir}/artsdsp
%attr(755,root,root) %{_bindir}/artsplay
%attr(755,root,root) %{_libdir}/libroarartsc.so.1
# compat links pointing to libroarartsc.so.1
%attr(755,root,root) %{_libdir}/libartsc.so.0
# needed?
%attr(755,root,root) %{_libdir}/libroarartsc.so
%attr(755,root,root) %{_libdir}/libartsc.so
%attr(755,root,root) %{_libdir}/libartsc.so.0.0
%attr(755,root,root) %{_libdir}/libartsc.so.0.0.0
%endif

%if %{with esd}
%files compat-esound
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/esd
%attr(755,root,root) %{_bindir}/esdcat
%attr(755,root,root) %{_bindir}/esddsp
%attr(755,root,root) %{_bindir}/esdfilt
%attr(755,root,root) %{_bindir}/esdmon
%attr(755,root,root) %{_bindir}/esdplay
%attr(755,root,root) %{_libdir}/libroaresd.so.1
# compat links pointing to libroaresd
%attr(755,root,root) %{_libdir}/libesd.so.0
# needed?
%attr(755,root,root) %{_libdir}/libroaresd.so
%attr(755,root,root) %{_libdir}/libesd.so
%attr(755,root,root) %{_libdir}/libesd.so.0.2
%attr(755,root,root) %{_libdir}/libesd.so.0.2.36
%endif

%if %{with nas}
%files compat-nas
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/audial
%attr(755,root,root) %{_bindir}/audiooss
%attr(755,root,root) %{_bindir}/auplay
%endif

%files compat-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libroaross.so.1
%attr(755,root,root) %{_libdir}/libroaross.so
# compat symlinks to libroaross.so.1
%attr(755,root,root) %{_libdir}/liboss.so
%attr(755,root,root) %{_libdir}/libossaudio.so

%if %{with pulseaudio}
%files compat-pulseaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pacat
%attr(755,root,root) %{_bindir}/padsp
%attr(755,root,root) %{_bindir}/paplay
%attr(755,root,root) %{_libdir}/libroarpulse.so.1
%attr(755,root,root) %{_libdir}/libroarpulse-simple.so.1
# compat links pointing to libroarpulse.so.1 and libroarpulse-simple.so.1
%attr(755,root,root) %{_libdir}/libpulse.so.0
%attr(755,root,root) %{_libdir}/libpulse-simple.so.0
# needed?
%attr(755,root,root) %{_libdir}/libroarpulse.so
%attr(755,root,root) %{_libdir}/libroarpulse-simple.so
%attr(755,root,root) %{_libdir}/libpulse.so
%attr(755,root,root) %{_libdir}/libpulse.so.0.1
%attr(755,root,root) %{_libdir}/libpulse.so.0.1.0
%attr(755,root,root) %{_libdir}/libpulse.so.0.4
%attr(755,root,root) %{_libdir}/libpulse.so.0.4.1
%attr(755,root,root) %{_libdir}/libpulse.so.0.12.2
%attr(755,root,root) %{_libdir}/libpulse-simple.so
%attr(755,root,root) %{_libdir}/libpulse-simple.so.0.0
%attr(755,root,root) %{_libdir}/libpulse-simple.so.0.0.0
%attr(755,root,root) %{_libdir}/libpulse-simple.so.0.0.1
%attr(755,root,root) %{_libdir}/libpulse-simple.so.0.0.2
%attr(755,root,root) %{_libdir}/libpulse-simple.so.0.0.3
%endif

%if %{with rsound}
%files compat-rsound
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ross
%attr(755,root,root) %{_bindir}/rsd
%attr(755,root,root) %{_bindir}/rsdplay
# not built yet
%attr(755,root,root) %{_libdir}/libroarrsound.so.1
%attr(755,root,root) %{_libdir}/libroarrsound.so
# compat symlinks to libroarrsound.so.1
%attr(755,root,root) %{_libdir}/librsound.so.0
%attr(755,root,root) %{_libdir}/librsound.so.1
%attr(755,root,root) %{_libdir}/librsound.so
%endif

%if %{with sndfile}
%files compat-sndfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libroarsndio.so.1
# compat symlink to libroarsndio.so.1
%attr(755,root,root) %{_libdir}/libsndio.so.0
# needed?
%attr(755,root,root) %{_libdir}/libroarsndio.so
%attr(755,root,root) %{_libdir}/libsndio.so
%endif

%if %{with yiff}
%files compat-yiff
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/yiff
%attr(755,root,root) %{_bindir}/yplay
%attr(755,root,root) %{_bindir}/yshutdown
%attr(755,root,root) %{_libdir}/libroaryiff.so.1
# compat symlink to libroaryiff.so.1
%attr(755,root,root) %{_libdir}/libY2.so.14
# needed?
%attr(755,root,root) %{_libdir}/libroaryiff.so
%attr(755,root,root) %{_libdir}/libY2.so
%endif

%if %{with xmms}
%files -n xmms-output-roar
%defattr(644,root,root,755)
%attr(755,root,root) %{xmms_output_plugindir}/libroar.so
%endif

%if %{with audacious}
%files -n audacious-output-roar
%defattr(644,root,root,755)
%{_libdir}/audacious/Output/libroar.so
%endif
