%define		_name ams
Summary:	Realtime modular synthesizer
Summary(pl):	Modularny syntezator dzia³aj±cy w czasie rzeczywistym
Name:		alsa-modular-synth
Version:	1.5.9
Release:	0.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://alsamodular.sourceforge.net/%{_name}-%{version}.tar.bz2
# Source0-md5:	432bc9d4aa3169da9fa4bf0381c5d02a
Source1:	%{name}.desktop
Patch0:		%{name}-build_fixes.patch
Patch1:		%{name}-fftw_hack.patch
URL:		http://alsamodular.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	fftw-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladspa-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AlsaModularSynth is a realtime modular synthesizer and effect
processor. It features:
- MIDI controlled modular software synthesis
- Realtime effect processing with capture from e.g. "Line In" or "Mic
  In"
- Full control of all synthesis and effect parameters via MIDI
- Integrated LADSPA Browser with search capability
- JACK Support

%description -l pl
AlsaModularSynth jest syntezatorem dzia³aj±cym w czasie rzeczywistym
i procesorem efektów. Zawiera:
- Kontrolowan± przez MIDI modularn± syntezê programow±
- Nak³adanie efektów w czasie rzeczywistym
- Pe³n± kontrolê syntez i efektów poprzez MIDI
- Zintegrowan± przegl±darkê LADSPA z mo¿liwo¶ci± wyszukiwania
- Wsparcie dla JACK

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__make} -f make_ams \
    CXXFLAGS="-DQT_THREAD_SUPPORT -I%{_includedir}/qt -I%{_prefix}/X11R6/include \
    -fno-exceptions -D_REENTRANT %{?debug:-DQT_NO_DEBUG} \
    -I. -g -Wall %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/ams,%{_desktopdir}}
install -c ams $RPM_BUILD_ROOT%{_bindir}
install -c *.ams $RPM_BUILD_ROOT%{_datadir}/ams
install -c %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/ams
%{_datadir}/ams/*.ams
%{_desktopdir}/%{name}.desktop
