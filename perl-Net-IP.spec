%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	IP
Summary:	Net::IP perl module
Summary(pl):	Modu³ perla Net::IP
Name:		perl-Net-IP
Version:	1.11
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch1:		%{name}-perl-path.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::IP Perl extension for the IP protocol.

%description -l pl
Net::IP - wsparcie dla protoko³u IP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch1 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
install ipcount $RPM_BUILD_ROOT%{_bindir}
install iptab $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Net/IP.pm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man3/*
