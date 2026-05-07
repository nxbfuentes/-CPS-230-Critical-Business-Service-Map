import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 1. Setup the canvas
fig, ax = plt.subplots(figsize=(12, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# 2. Helper function for nodes (Fixed font property)
def draw_node(x, y, w, h, text, color, ls='-', label="", label_color='blue'):
    rect = patches.FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=0.1",
                                 fc=color, ec="black", lw=2, ls=ls)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=9, fontweight='bold')
    if label:
        ax.text(x, y + h/2 + 0.3, label, ha='center', color=label_color, fontsize=8, style='italic')

# 3. Draw the map components
draw_node(1, 4, 1.5, 1.2, "Staff Member\n(Member Officer)", "skyblue")
draw_node(3.5, 6, 1.8, 1, "Internal Helpdesk\n(Service Desk)", "#ecf0f1", label="Dependency: PEOPLE")
draw_node(3.5, 4, 1.8, 1, "Azure AD\n(Cloud Directory)", "#ecf0f1", label="Dependency: INTERNAL TECH")
draw_node(6.5, 4, 2, 1.2, "Primary MFA\n(Third-Party SaaS)", "#e74c3c", label="CRITICAL SPOF", label_color='red')
draw_node(6.5, 2, 2, 1, "Backup MFA\n(MS Authenticator)", "#2ecc71", ls="--", label="PROPOSED RESILIENCE UPLIFT", label_color='green')
draw_node(9.2, 4, 1.5, 1.2, "Banking CRM\n& Workforce Systems", "#f1c40f")

# 4. Connections
def connect(x1, y1, x2, y2, ls='-'):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", lw=1.5, ls=ls, color='black'))

connect(1.75, 4.2, 2.6, 5.8)
connect(1.75, 4, 2.6, 4)
connect(3.5, 5.5, 3.5, 4.5)
connect(4.4, 4, 5.5, 4)
connect(7.5, 4, 8.45, 4)
connect(4.4, 3.8, 5.5, 2.2, ls='--')
connect(7.5, 2.2, 8.5, 3.6, ls='--')

plt.title("CPS 230 Service Dependency Map: Employee System Access Lifecycle", fontsize=14, fontweight='bold', pad=20)
ax.text(0.5, 0.5, "* Red Box indicates Third-Party dependency with no current redundancy.\n* Dashed lines indicate proposed resilience 'uplift' to meet CPS 230 standards.",
        fontsize=9, style='italic', bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()
plt.savefig('cps230_dependency_map.png', bbox_inches='tight')
print("Diagram generated.")
