%define		_name ams
Summary:	Realtime modular synthesizer
Summary(pl):	Modularny syntezator dzia³aj±cy w czasie rzeczywistym
Name:		alsa-modular-synth
Version:	1.5.12
Release:	0.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://alsamodular.sourceforge.net/%{_name}-%{version}.tar.bz2
# Source0-md5:	ef366e3b4a1c0519420c8736d1445795
Source1:	%{name}.desktop
Patch0:		%{name}-build_fixes.patch
Patch1:		%{name}-fftw_hack.patch
URL:		http://alsamodular.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	fftw-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.74.1
BuildRequires:	qt-devel >= 3.0.5
Requires:	ladspa
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AlsaModularSynth is a realtime modular synthesizer and effect
processor. It features:
- MIDI controlled modular software synthesis
- Realtime effect processing
- Full control of all synthesis and effect parameters via MIDI
- Integrated LADSPA Browser with search capability
- JACK Support

%description -l pl
AlsaModularSynth jest syntezatorem i procesorem efektów dzia³aj±cym w
czasie rzeczywistym. Zawiera:
- kontrolowan± przez MIDI modularn± syntezê programow±
- nak³adanie efektów w czasie rzeczywistym
- pe³n± kontrolê syntezy i efektów poprzez MIDI
- zintegrowan± przegl±darkê LADSPA z mo¿liwo¶ci± wyszukiwania
- wsparcie dla JACK

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
    CXXFLAGS="-DQT_THREAD_SUPPORT -I%{_includedir}/qt \
    -I/usr/X11R6/include \
    -fno-exceptions -D_REENTRANT %{?debug:-DQT_NO_DEBUG} \
    -I. -Wall %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/ams,%{_desktopdir}}

install ams $RPM_BUILD_ROOT%{_bindir}
install *.ams $RPM_BUILD_ROOT%{_datadir}/ams
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/ams
%{_datadir}/ams/*.ams
%{_desktopdir}/%{name}.desktop
