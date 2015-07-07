Name:           gawk
Url:            http://www.gnu.org/software/gawk/
Provides:       awk
BuildRequires:  automake >= 1.13
BuildRequires:  makeinfo
Version:        4.1.1
Release:        0
Summary:        GNU awk
License:        GPL-3.0+
Group:          Base/Utilities
Source:         gawk-%{version}.tar.bz2
Source1001:     gawk.manifest

# Temporary
Provides:       /bin/awk
Provides:       /bin/gawk

%description
GNU awk is upwardly compatible with the System V Release 4 awk.  It is
almost completely POSIX 1003.2 compliant.

%package devel
License:        GPL-3.0+
Summary:        Utilities for awk scripts development
Group:          Base/Utilities
Requires:       gawk

%description devel
Package contains tools for debugging and profiling of awk scripts

%package extras
License:        TIZEN-Public-Domain
Summary:        Files not essential for basic AWK usage
Group:          Base/Utilities
Requires:       gawk

%description extras
Package contains igawk utility which allows to include source files in
AWK programs. Several reusable AWK scripts and their dependencies are
also included.


%prep
%setup -q
cp %{SOURCE1001} .

%build
AUTOPOINT=true autoreconf --force --install
%configure --libexecdir=%{_libdir} --disable-nls
%if %do_profiling
  %__make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS %cflags_profile_generate"
  %__make check
  %__make clean
  %__make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS %cflags_profile_feedback"
%else
  %__make %{?_smp_mflags}
%endif

%check
%__make check

%install
%make_install


%docs_package

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_bindir}/awk
%{_bindir}/gawk*
%{_libdir}/gawk/*.so

%files devel
%defattr(-,root,root)
%{_includedir}/gawkapi.h

%files extras
%defattr(-,root,root)
%{_bindir}/igawk
%{_libdir}/awk
%{_datadir}/awk
