%include	/usr/lib/rpm/macros.perl
%define	pdir	GD
%define	pnam	TextUtil
Summary:	GD::TextUtil perl module
Summary(pl):	Modu³ perla GD::TextUtil
Name:		perl-GD-TextUtil
Version:	0.83
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::TextUtil perl module - Text utilities for use with the GD drawing
package.

%description -l pl
Modu³ perla GD::TextUtil - narzêdzia do obróbki tekstu przeznaczone do
u¿ywania z pakietem rysuj±cym GD.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/GD/Text.pm
%{perl_sitelib}/GD/Text
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
