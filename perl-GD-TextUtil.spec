%include	/usr/lib/rpm/macros.perl
Summary:	GD-TextUtil perl module
Summary(pl):	Modu³ perla GD-TextUtil
Name:		perl-GD-TextUtil
Version:	0.80
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/GD/GDTextUtil-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GD
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD-TextUtil perl module.

%description -l pl
Modu³ perla GD-TextUtil.

%prep
%setup -q -n GDTextUtil-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/GD/Text.pm
%{perl_sitelib}/GD/Text
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
