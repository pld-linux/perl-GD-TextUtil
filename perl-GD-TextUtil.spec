%include	/usr/lib/rpm/macros.perl
Summary:	GD-TextUtil perl module
Summary(pl):	Modu³ perla GD-TextUtil
Name:		perl-GD-TextUtil
Version:	0.70
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/GD/GDTextUtil-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-GD
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD-TextUtil perl module

%description -l pl
Modu³ perla GD-TextUtil

%prep
%setup -q -n GDTextUtil-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}

make install DESTDIR=$RPM_BUILD_ROOT
install demo/* $RPM_BUILD_ROOT/usr/src/examples/%{name}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/GDTextUtil
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/GD/Text.pm
%{perl_sitelib}/GD/Text
%{perl_sitearch}/auto/GDTextUtil

%{_mandir}/man3/*

/usr/src/examples/%{name}
