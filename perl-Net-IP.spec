%include	/usr/lib/rpm/macros.perl
Summary:	Net-IP perl module
Summary(pl):	Modu³ perla Net-IP
Name:		perl-Net-IP
Version:	1.0
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-IP-%{version}.tar.gz
Patch0:		%{name}-doc.patch
Patch1:		%{name}-perl-path.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-iP Perl extension for the IP protocol.

%description -l pl
Net-IP - wsparcie dla protoko³u IP.

%prep
%setup -q -n Net-IP-%{version}
%patch0 -p1
%patch1 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
install ipcount.pl $RPM_BUILD_ROOT%{_bindir}

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Net/IP.pm
%attr(755,root,root) %{_bindir}/*.pl
%{_mandir}/man3/*
