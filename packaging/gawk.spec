Name:           gawk
Url:            http://www.gnu.org/software/gawk/
Provides:       awk
BuildRequires:  automake
BuildRequires:  makeinfo
Version:        4.0.1
Release:        0
Summary:        GNU awk
License:        GPL-3.0+
Group:          Productivity/Text/Utilities
Source:         gawk-%{version}.tar.bz2

# Temporary
Provides:       /bin/awk
Provides:       /bin/gawk

%description
GNU awk is upwardly compatible with the System V Release 4 awk.  It is
almost completely POSIX 1003.2 compliant.

%prep
%setup -q
#rm -f regex.[ch]
chmod -x COPYING
# force rebuild with non-broken makeinfo
rm -f doc/*.info

%build
AUTOPOINT=true autoreconf --force --install
%configure --libexecdir=%{_libdir} --disable-nls
%if %do_profiling
  make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS %cflags_profile_generate"
  make check
  make clean
  make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS %cflags_profile_feedback"
%else
  make %{?_smp_mflags}
%endif

%check
make check

%install
%make_install


%docs_package

%files 
%defattr(-,root,root)
%license COPYING
%{_bindir}/awk
%{_bindir}/dgawk
%{_bindir}/gawk*
%{_bindir}/igawk
%{_bindir}/pgawk*
%{_libdir}/awk
/usr/share/awk

%changelog
