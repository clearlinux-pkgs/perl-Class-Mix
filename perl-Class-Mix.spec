#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Mix
Version  : 0.006
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Class-Mix-0.006.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Class-Mix-0.006.tar.gz
Summary  : 'dynamic class mixing'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Params::Classify)

%description
NAME
Class::Mix - dynamic class mixing
DESCRIPTION
The "mix_class" function provided by this module dynamically generates
`anonymous' classes with specified inheritance.

%package dev
Summary: dev components for the perl-Class-Mix package.
Group: Development
Provides: perl-Class-Mix-devel = %{version}-%{release}

%description dev
dev components for the perl-Class-Mix package.


%prep
%setup -q -n Class-Mix-0.006

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Class/Mix.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Mix.3
