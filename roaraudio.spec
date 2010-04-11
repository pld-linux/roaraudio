# TODO
# - see HACKING for packaging suggestions
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
BuildRequires:	esound-devel
BuildRequires:	libao-devel
BuildRequires:	libdnet-devel
BuildRequires:	libfishsound-devel
BuildRequires:	libggz-devel
BuildRequires:	libshout-devel
#BuildRequires:	libslp-dev
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	openssl-devel
BuildRequires:	sed >= 4.0
BuildRequires:	speex-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RoarAudio is a server for audio mixing. It's main purpose is to mix
audio from different clients before sending it to it's outputs. Those
outputs may for example be soundcards. It also supports network
clients because of it's full network transparency.

%prep
%setup -q -n %{name}-%{version}%{subver}

find -name Makefile | xargs grep -l -- '-g -Wall -O2' | xargs sed -i -e 's,-g -Wall -O2,%{rpmcflags},'

%build
# NOTE: not autoconf derivered configure
./configure \
	--cc "%{__cc}" \
	--prefix %{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING README TODO
