Name:           rust-srpm-macros
Version:        13
Release:        1
Summary:        RPM macros for building Rust source packages
Group:          System/Packaging
License:        MIT
URL:            https://pagure.io/fedora-rust/rust2rpm
Source:         https://releases.pagure.org/fedora-rust/rust2rpm/rust2rpm-%{version}.tar.xz

BuildArch:      noarch

%description
RPM macros for building Rust source packages

%prep
%autosetup -n rust2rpm-%{version} -p1
# https://pagure.io/koji/issue/659
sed -i -e 's/i686/%%{ix86}/' data/macros.rust-srpm
sed -i -e 's/x86_64/%%{x86_64}/' data/macros.rust-srpm

%install
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} data/macros.rust-srpm

%files
%license LICENSE
%{_rpmmacrodir}/macros.rust-srpm
