Summary:	A plugin for the Xfce4 panel displaying keyboard layout
Name:		xfce4-xkb-plugin
Version:	0.4.3
Release:	%mkrel 5
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xkb-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-xkb-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	perl(XML::Parser)
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
%{_datadir}/*/*/xkb-plugin.desktop
%{_libdir}/xfce4/panel-plugins/
