%define	upstream_name	 Net-SSH-Perl
%define upstream_version 1.36

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Perl client Interface to SSH
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Net/Net-SSH-Perl-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Math::Pari)
BuildRequires:	perl(Math::GMP)
BuildRequires:	perl(String::CRC32)
BuildRequires:	perl(Convert::PEM)
BuildRequires:	perl(Crypt::IDEA)
BuildRequires:	perl(Crypt::DH)
BuildRequires:	perl(Crypt::DSA)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Digest::HMAC)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Digest::BubbleBabble)
BuildRequires:	perl(Crypt::RSA)
BuildArch:	noarch

%description
Net::SSH::Perl is an all-Perl module implementing an SSH
(Secure Shell) client. It is compatible with both the SSH-1
and SSH-2 protocols.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
# test hang... :\
# make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Net
%{_mandir}/man*/*


%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.340.0-1mdv2010.0
+ Revision: 407848
- rebuild using %%perl_convert_version

* Tue Feb 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.34-1mdv2009.1
+ Revision: 336949
- update to new version 1.34

* Wed Oct 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.33-1mdv2009.1
+ Revision: 296404
- update to new version 1.33

* Mon Oct 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.32-1mdv2009.1
+ Revision: 295507
- update to new version 1.32

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.31-1mdv2009.1
+ Revision: 292267
- update to new version 1.31

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.30-5mdv2009.0
+ Revision: 241800
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.30-3mdv2008.0
+ Revision: 25198
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.30-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Wed Apr 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.30-1mdk
- New release 1.30

* Mon Oct 10 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.29-1mdk
- new version
- %%mkrel
- spec cleanup
- better url
- fix sources url
- fix directory ownership
- make test in %%check

* Thu May 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.28-1mdk
- 1.28

* Fri Feb 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.27-1mdk
- 1.27

* Sat Feb 05 2005 Sylvie Terjan <erinmargault@mandrake.org> 1.26-1mdk
- 1.26
- rebuild for new perl

* Thu Jun 03 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 1.25-1mdk
- 1.25
- drop prefix tag
- cosmetics

* Mon Dec 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.24-1mdk
- 1.24

* Sun Nov 09 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 1.23-1mdk
- First MandrakeSoft Package



