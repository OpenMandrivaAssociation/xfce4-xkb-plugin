Summary:	A plugin for the Xfce4 panel displaying keyboard layout
Name:		xfce4-xkb-plugin
Version:	0.5.3.3
Release:	%mkrel 4
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xkb-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-xkb-plugin/%{name}-%{version}.tar.bz2
Patch0:		xfce4-xkb-plugin-0.5.3.3-libxklavier5.0.patch
Patch1:		xfce4-xkb-plugin-0.5.3.3-fix-crashes.patch
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	intltool
BuildRequires:	libxklavier-devel >= 5.0
BuildRequires:	librsvg2-devel
BuildRequires:	libwnck-devel
Requires:	xfce4-panel >= 4.4.2
Obsoletes:	xfce-xkb-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A plugin for the Xfce4 panel displaying keyboard layout.
The plugin may be used as an indicator for the current layout
and to switch layouts.
The layouts must be defined either in XF86Config or by 
xetskbmap tool.

%prep
%setup -q
%patch0 -p1 -b .libxklavier5.0
%patch1 -p1
autoconf

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

# remove unneeded devel files
rm -f %{buildroot}/%{_libdir}/xfce4/panel-plugins/*.a

%find_lang %{name}

%clean
rm -rf  %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%dir %{_datadir}/xfce4/xkb
%{_datadir}/xfce4/xkb/*
%{_datadir}/xfce4/panel-plugins/xkb-plugin.desktop
%{_libdir}/xfce4/panel-plugins/
